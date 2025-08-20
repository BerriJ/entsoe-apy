from functools import wraps

from .utils import check_date_range_limit, merge_documents, split_date_range


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
        
        # If no period parameters, just call the function normally
        if period_start is None or period_end is None:
            return func(params, *args, **kwargs)
        
        # Check if the range exceeds the limit (1 year = 365 days)
        if check_date_range_limit(period_start, period_end, max_days=365):
            # Split the range and make recursive calls
            pivot_date, _ = split_date_range(period_start, period_end)
            
            # Create new params for the first half
            params1 = params.copy()
            params1["periodEnd"] = pivot_date
            
            # Create new params for the second half  
            params2 = params.copy()
            params2["periodStart"] = pivot_date
            
            # Recursively call for both halves
            result1 = range_wrapper(params1, *args, **kwargs)
            result2 = range_wrapper(params2, *args, **kwargs)
            
            # Merge the results
            return merge_documents(result1, result2)
        else:
            # Range is within limit, make the API call
            return func(params, *args, **kwargs)

    return range_wrapper
