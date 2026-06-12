import re
from datetime import datetime

def validate_date(date_str):
    """Validates date string in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def format_header(title):
    """Returns a formatted header string."""
    line = "=" * len(title)
    return f"\n{line}\n{title}\n{line}"
