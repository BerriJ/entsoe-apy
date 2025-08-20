from functools import wraps

from .utils import check_date_range_limit, merge_documents, split_date_range


class AcknowledgementDocumentError(Exception):
    """Raised when the API returns an acknowledgement document indicating an error."""

    pass


def range_limited(func):
    """
    Decorator that handles range limit errors by splitting the requested period
    and merging the results.

    Catches a RangeLimitError, splits the requested period in two and tries
    again. Finally it merges the results using merge_documents.
    """

    @wraps(func)
    def range_wrapper(params, *args, **kwargs):
        # Extract period parameters from params dict
        period_start = params.get("periodStart")
        period_end = params.get("periodEnd")

        # print(f"[RANGE_WRAPPER] Function: {func.__name__}")
        # print(f"[RANGE_WRAPPER] Initial range: {period_start} to {period_end}")

        # If no period parameters, just call the function normally
        if period_start is None or period_end is None:
            # print("[RANGE_WRAPPER] No period parameters found, calling directly")
            return func(params, *args, **kwargs)

        # Check if the range exceeds the limit (1 year = 365 days)
        if check_date_range_limit(period_start, period_end, max_days=365):
            # print("[RANGE_WRAPPER] Range exceeds 365 days, splitting...")

            # Split the range and make recursive calls
            pivot_date, _ = split_date_range(period_start, period_end)
            # print(f"[RANGE_WRAPPER] Split at pivot: {pivot_date}")

            # Create new params for the first half
            params1 = params.copy()
            params1["periodEnd"] = pivot_date
            # print(
            #     f"[RANGE_WRAPPER] First half: {params1['periodStart']} to "
            #     f"{params1['periodEnd']}"
            # )

            # Create new params for the second half
            params2 = params.copy()
            params2["periodStart"] = pivot_date
            # print(
            #     f"[RANGE_WRAPPER] Second half: {params2['periodStart']} to "
            #     f"{params2['periodEnd']}"
            # )

            # Recursively call for both halves
            # print("[RANGE_WRAPPER] Making recursive call for first half...")
            result1 = range_wrapper(params1, *args, **kwargs)
            # print("[RANGE_WRAPPER] Making recursive call for second half...")
            result2 = range_wrapper(params2, *args, **kwargs)

            return merge_documents(result1, result2)

        else:
            # Range is within limit, make the API call
            # print("[RANGE_WRAPPER] Range within 365 days, making API call")
            return func(params, *args, **kwargs)

    return range_wrapper


def Acknowledgement(func):
    @wraps(func)
    def ack_wrapper(params, *args, **kwargs):
        name, response = func(params, *args, **kwargs)
        if "acknowledgementdocument" in name.lower():
            reason = response.reason[0].text
            if "No matching data found" in reason:
                print(reason)
                return None, None
            else:
                raise AcknowledgementDocumentError(response.reason)
        return name, response

    return ack_wrapper


def pagination(func):
    @wraps(func)
    def pagination_wrapper(params, *args, **kwargs):
        # Check if offset is in params (indicating pagination is needed)
        if "offset" not in params:
            return func(params, *args, **kwargs)

        results = []
        for offset in range(0, 4801, 100):  # 0 to 4800 in increments of 100
            # Create new params with current offset
            paginated_params = params.copy()
            paginated_params["offset"] = offset

            try:
                name, response = func(paginated_params, *args, **kwargs)

                # If response is None, we've reached the end
                if response is None:
                    break

                results.append(response)

            except Exception:
                # If we get an error (like no matching data), break the loop
                break

        # If no results were collected, return None
        if not results:
            return None, None

        # If only one result, return it directly
        if len(results) == 1:
            return name, results[0]

        # Merge all results using merge_documents
        merged_result = results[0]
        for result in results[1:]:
            merged_result = merge_documents(merged_result, result)

        return name, merged_result

    return pagination_wrapper
