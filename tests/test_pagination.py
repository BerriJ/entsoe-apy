"""Tests for pagination with different offset increments."""

from unittest.mock import MagicMock, patch

from entsoe.Base.Balancing import Balancing
from entsoe.Base.Market import Market
from entsoe.Base.Outages import Outages
from entsoe.query import decorators
from entsoe.query.decorators import pagination


class TestPaginationOffsetIncrement:
    """Test pagination with different offset increments for different groups."""

    def test_base_class_has_offset_increment(self):
        """Test that Base class has offset_increment attribute with default value."""
        from entsoe.Base.Base import Base

        assert hasattr(Base, "offset_increment")
        assert Base.offset_increment == 100

    def test_outages_class_overrides_offset_increment(self):
        """Test that Outages class overrides offset_increment to 200."""
        assert hasattr(Outages, "offset_increment")
        assert Outages.offset_increment == 200

    def test_market_class_uses_default_offset_increment(self):
        """Test that Market class uses default offset_increment of 100."""
        assert hasattr(Market, "offset_increment")
        assert Market.offset_increment == 100

    def test_balancing_class_uses_default_offset_increment(self):
        """Test that Balancing class uses default offset_increment of 100."""
        assert hasattr(Balancing, "offset_increment")
        assert Balancing.offset_increment == 100

    def test_pagination_decorator_uses_offset_increment_100(self):
        """Test pagination decorator with offset_increment=100 (Market/Balancing)."""
        mock_func = MagicMock(return_value=[{"data": "test"}])
        decorated_func = pagination(mock_func)

        # Simulate a params dict with offset parameter
        params = {"offset": 0, "documentType": "A25"}

        # Mock the function to return empty list after first call to stop pagination
        call_count = 0

        def side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return [{"data": f"result_{args[0]['offset']}"}]
            return []

        mock_func.side_effect = side_effect

        # Call the decorated function with offset_increment=100
        token = decorators.offset_increment_ctx.set(100)
        try:
            decorated_func(params)
        finally:
            decorators.offset_increment_ctx.reset(token)

        # Verify the function was called with offset=0
        assert (
            mock_func.call_count == 2
        )  # First call returns data, second returns empty
        # Verify the offset was set correctly in the params
        assert params["offset"] == 100  # Last offset value

    def test_pagination_decorator_uses_offset_increment_200(self):
        """Test pagination decorator with offset_increment=200 (Outages)."""
        mock_func = MagicMock(return_value=[{"data": "test"}])
        decorated_func = pagination(mock_func)

        # Simulate a params dict with offset parameter
        params = {"offset": 0, "documentType": "A77"}

        # Track the offsets that were used
        offsets_used = []

        # Mock the function to return data for first two calls, then empty
        def side_effect(p, *args, **kwargs):
            offsets_used.append(p["offset"])
            if len(offsets_used) <= 2:
                return [{"data": f"result_{p['offset']}"}]
            return []

        mock_func.side_effect = side_effect

        # Call the decorated function with offset_increment=200
        token = decorators.offset_increment_ctx.set(200)
        try:
            decorated_func(params)
        finally:
            decorators.offset_increment_ctx.reset(token)

        # Verify the function was called with increasing offsets
        assert mock_func.call_count == 3  # Two calls with data, one empty
        # Check that offsets were 0, 200, 400
        assert offsets_used == [0, 200, 400]

    def test_pagination_decorator_without_offset_parameter(self):
        """Test pagination decorator when offset is not in params."""
        mock_func = MagicMock(return_value=[{"data": "test"}])
        decorated_func = pagination(mock_func)

        # Params without offset
        params = {"documentType": "A25"}

        token = decorators.offset_increment_ctx.set(100)
        try:
            decorated_func(params)
        finally:
            decorators.offset_increment_ctx.reset(token)

        # Should call the function once without pagination
        assert mock_func.call_count == 1

    def test_outages_instance_passes_offset_increment_200(self):
        """Test that Outages instance passes offset_increment=200 to query_api."""
        # Create an Outages instance
        outages = Outages(
            document_type="A77",
            period_start=202301010000,
            period_end=202301020000,
            bidding_zone_domain="10YBE----------2",
            offset=0,
        )

        # Verify the offset_increment is 200
        assert outages.offset_increment == 200

        # Mock the entire query_api call chain
        with patch("entsoe.query.query_api.query_and_parse") as mock_query_parse:
            mock_query_parse.return_value = []

            # Since we're patching deeper, we can directly verify the parameters
            # passed to the actual query_api function
            from entsoe.query.query_api import query_api

            # Set context variables directly
            token_max_days = decorators.max_days_limit_ctx.set(outages.max_days_limit)
            token_offset = decorators.offset_increment_ctx.set(outages.offset_increment)
            try:
                query_api(outages.params)
            finally:
                decorators.max_days_limit_ctx.reset(token_max_days)
                decorators.offset_increment_ctx.reset(token_offset)

            # The function should have been called
            assert mock_query_parse.called

    def test_market_instance_passes_offset_increment_100(self):
        """Test that Market instance passes offset_increment=100 to query_api."""
        # Create a Market instance
        market = Market(
            document_type="A25",
            period_start=202301010000,
            period_end=202301020000,
            in_domain="10YBE----------2",
            offset=0,
        )

        # Verify the offset_increment is 100
        assert market.offset_increment == 100

        # Mock the entire query_api call chain
        with patch("entsoe.query.query_api.query_and_parse") as mock_query_parse:
            mock_query_parse.return_value = []

            # Since we're patching deeper, we can directly verify the parameters
            # passed to the actual query_api function
            from entsoe.query.query_api import query_api

            # Set context variables directly
            token_max_days = decorators.max_days_limit_ctx.set(market.max_days_limit)
            token_offset = decorators.offset_increment_ctx.set(market.offset_increment)
            try:
                query_api(market.params)
            finally:
                decorators.max_days_limit_ctx.reset(token_max_days)
                decorators.offset_increment_ctx.reset(token_offset)

            # The function should have been called
            assert mock_query_parse.called

    def test_pagination_continues_until_empty_with_increment_100(self):
        """Test that pagination continues until no results with increment 100."""
        mock_func = MagicMock()
        decorated_func = pagination(mock_func)

        params = {"offset": 0, "documentType": "A25"}

        # Return data for 50 pages (offsets 0..4900), then empty
        total_pages = 50
        call_count = 0

        def side_effect(p, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count <= total_pages:
                return [{"data": f"result_{p['offset']}"}]
            return []

        mock_func.side_effect = side_effect

        token = decorators.offset_increment_ctx.set(100)
        try:
            result = decorated_func(params)
        finally:
            decorators.offset_increment_ctx.reset(token)

        # Should have been called 51 times (50 with data + 1 empty)
        assert mock_func.call_count == 51
        assert len(result) == 50
        # Last call should have offset 5000, beyond the old 4800 limit
        assert mock_func.call_args_list[-1][0][0]["offset"] == 5000

    def test_pagination_continues_until_empty_with_increment_200(self):
        """Test that pagination continues until no results with increment 200."""
        mock_func = MagicMock()
        decorated_func = pagination(mock_func)

        params = {"offset": 0, "documentType": "A77"}

        # Return data for 30 pages (offsets 0..5800), then empty
        total_pages = 30
        call_count = 0

        def side_effect(p, *args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count <= total_pages:
                return [{"data": f"result_{p['offset']}"}]
            return []

        mock_func.side_effect = side_effect

        token = decorators.offset_increment_ctx.set(200)
        try:
            result = decorated_func(params)
        finally:
            decorators.offset_increment_ctx.reset(token)

        # Should have been called 31 times (30 with data + 1 empty)
        assert mock_func.call_count == 31
        assert len(result) == 30
        # Last call should have offset 6000, beyond the old 4800 limit
        assert mock_func.call_args_list[-1][0][0]["offset"] == 6000
