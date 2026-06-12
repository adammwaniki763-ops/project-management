
from ..utils import validate_date

def test_validate_date_valid():
    assert validate_date("2024-01-01") is True

def test_validate_date_invalid():
    assert validate_date("2024-13-01") is False
    assert validate_date("01-01-2024") is False
    assert validate_date("not-a-date") is False
