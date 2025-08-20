"""Tests for datetime validation functionality."""

from datetime import datetime
from unittest.mock import patch
import warnings

import pytest

from entsoe.Base import Base, ValidationError


class TestDatetimeValidation:
    """Test cases for datetime parameter validation."""

    def test_validate_datetime_param_valid(self):
        """Test validation passes for valid datetime values."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        # Valid datetime: 2020-12-31 23:00
        result = base.validate_datetime_param(202012312300, "test_param")
        assert result == 202012312300

    def test_validate_datetime_param_none(self):
        """Test validation passes for None values."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        result = base.validate_datetime_param(None, "test_param")
        assert result is None

    def test_validate_datetime_param_invalid_format(self):
        """Test validation fails for invalid datetime formats."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        # Too short
        with pytest.raises(ValidationError) as exc_info:
            base.validate_datetime_param(20201231, "test_param")
        assert "Invalid datetime format" in str(exc_info.value)
        assert "Expected YYYYMMDDHHMM format (12 digits)" in str(exc_info.value)

        # Invalid date
        with pytest.raises(ValidationError) as exc_info:
            base.validate_datetime_param(202013312300, "test_param")
        assert "Invalid datetime format" in str(exc_info.value)

    def test_validate_datetime_param_before_2014(self):
        """Test warning and correction for dates before 2014-01-01."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # Date before 2014: 2013-12-31 23:59
            result = base.validate_datetime_param(201312312359, "test_param")
            
            assert result == 202401010000  # Should be set to 2024-01-01 00:00
            assert len(w) == 1
            assert "before 2014-01-01" in str(w[0].message)
            assert "Setting to 2024-01-01 00:00" in str(w[0].message)

    @patch('entsoe.Base.Base.datetime')
    def test_validate_datetime_param_after_current_time(self, mock_datetime):
        """Test warning and correction for dates after current time."""
        # Mock current time to be 2023-06-15 12:30
        mock_now = datetime(2023, 6, 15, 12, 30)
        mock_datetime.now.return_value = mock_now
        mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            # Date in future: 2024-01-01 00:00
            result = base.validate_datetime_param(202401010000, "test_param")
            
            assert result == 202306151230  # Should be set to current time
            assert len(w) == 1
            assert "after current time" in str(w[0].message)
            assert "Setting to current time" in str(w[0].message)

    def test_add_period_params_valid(self):
        """Test add_period_params with valid datetime values."""
        base = Base(
            document_type="A44",
            security_token="test_token",
            period_start=202012312300,
            period_end=202101022300,
        )

        assert base.params["periodStart"] == 202012312300
        assert base.params["periodEnd"] == 202101022300

    def test_add_period_params_start_after_end(self):
        """Test error when period_start is after period_end."""
        with pytest.raises(ValidationError) as exc_info:
            Base(
                document_type="A44",
                security_token="test_token",
                period_start=202101022300,  # After end
                period_end=202012312300,    # Before start
            )

        assert "period_start" in str(exc_info.value)
        assert "cannot be after period_end" in str(exc_info.value)

    def test_add_period_params_with_none_values(self):
        """Test add_period_params with None values."""
        base = Base(
            document_type="A44",
            security_token="test_token",
            period_start=None,
            period_end=None,
        )

        assert "periodStart" not in base.params
        assert "periodEnd" not in base.params

    def test_add_period_params_one_none_value(self):
        """Test add_period_params with one None value."""
        base = Base(
            document_type="A44",
            security_token="test_token",
            period_start=202012312300,
            period_end=None,
        )

        assert base.params["periodStart"] == 202012312300
        assert "periodEnd" not in base.params

    def test_period_validation_corrects_old_dates(self):
        """Test that old dates are corrected during initialization."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            base = Base(
                document_type="A44",
                security_token="test_token",
                period_start=201312312300,  # 2013 date
                period_end=202101022300,
            )

            # Check that old date was corrected
            assert base.params["periodStart"] == 202401010000
            assert base.params["periodEnd"] == 202101022300
            assert len(w) == 1
            assert "before 2014-01-01" in str(w[0].message)

    @patch('entsoe.Base.Base.datetime')
    def test_period_validation_corrects_future_dates(self, mock_datetime):
        """Test that future dates are corrected during initialization."""
        # Mock current time to be 2023-06-15 12:30
        mock_now = datetime(2023, 6, 15, 12, 30)
        mock_datetime.now.return_value = mock_now
        mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            base = Base(
                document_type="A44",
                security_token="test_token",
                period_start=202012312300,
                period_end=202501010000,  # Future date
            )

            # Check that future date was corrected
            assert base.params["periodStart"] == 202012312300
            assert base.params["periodEnd"] == 202306151230
            assert len(w) == 1
            assert "after current time" in str(w[0].message)

    def test_boundary_dates(self):
        """Test boundary dates (exactly 2014-01-01 and current time)."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        # Exactly 2014-01-01 should be valid (no warning)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = base.validate_datetime_param(201401010000, "test_param")
            assert result == 201401010000
            assert len(w) == 0  # No warnings

    def test_explicit_period_params_call(self):
        """Test calling add_period_params explicitly."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        # Test with valid periods
        base.add_period_params(
            period_start=202012312300,
            period_end=202101022300
        )

        assert base.params["periodStart"] == 202012312300
        assert base.params["periodEnd"] == 202101022300

        # Test error case
        with pytest.raises(ValidationError):
            base.add_period_params(
                period_start=202101022300,  # After end
                period_end=202012312300     # Before start
            )

    def test_add_update_params_validation(self):
        """Test validation of period_start_update and period_end_update."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        # Test with valid update periods
        base.add_update_params(
            period_start_update=202012312300,
            period_end_update=202101022300
        )

        assert base.params["periodStartUpdate"] == 202012312300
        assert base.params["periodEndUpdate"] == 202101022300

    def test_add_update_params_start_after_end(self):
        """Test error when period_start_update is after period_end_update."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        with pytest.raises(ValidationError) as exc_info:
            base.add_update_params(
                period_start_update=202101022300,  # After end
                period_end_update=202012312300     # Before start
            )

        assert "period_start_update" in str(exc_info.value)
        assert "cannot be after period_end_update" in str(exc_info.value)

    def test_add_update_params_with_old_dates(self):
        """Test that old dates in update parameters are corrected."""
        base = Base(
            document_type="A44",
            security_token="test_token",
        )

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            
            base.add_update_params(
                period_start_update=201312312300,  # 2013 date
                period_end_update=202101022300,
            )

            # Check that old date was corrected
            assert base.params["periodStartUpdate"] == 202401010000
            assert base.params["periodEndUpdate"] == 202101022300
            assert len(w) == 1
            assert "before 2014-01-01" in str(w[0].message)