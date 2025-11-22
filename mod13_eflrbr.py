"""
Unit tests for the five inputs from Project 3 (Stock Data Visualizer).

Constraints:
- symbol: capitalized, 1-7 alpha characters
- chart type: 1 numeric character, '1' or '2'
- time series: 1 numeric character, '1'-'4'
- start date: date type YYYY-MM-DD
- end date: date type YYYY-MM-DD
"""

import re
import unittest
from datetime import datetime

# Validation helper functions (the "units" we test)

def validate_symbol(symbol: str) -> bool:
    """
    Valid if:
      - length between 1 and 7
      - only letters A–Z
      - all uppercase
    """
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))

def validate_chart_type(chart_type: str) -> bool:
    """
    Valid if:
      - exactly one character
      - '1' or '2'
    """
    return chart_type in ("1", "2")

def validate_time_series(time_series: str) -> bool:
    """
    Valid if:
      - exactly one character
      - '1', '2', '3', or '4'
    """
    return time_series in ("1", "2", "3", "4")

def validate_date(date_str: str) -> bool:
    """
    Valid if:
      - matches format YYYY-MM-DD
      - is a real calendar date
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Unit tests

class TestProject3InputValidation(unittest.TestCase):

    # symbol tests

    def test_symbol_valid_single_letter(self):
        self.assertTrue(validate_symbol("A"))

    def test_symbol_valid_max_length(self):
        # 7 characters, all uppercase letters
        self.assertTrue(validate_symbol("ABCDEFG"))

    def test_symbol_invalid_too_long(self):
        # More than 7 characters is invalid
        self.assertFalse(validate_symbol("ABCDEFGH"))

    def test_symbol_invalid_lowercase(self):
        self.assertFalse(validate_symbol("aapl"))

    def test_symbol_invalid_mixed_case(self):
        self.assertFalse(validate_symbol("AaPL"))

    def test_symbol_invalid_with_digits(self):
        self.assertFalse(validate_symbol("AAPL1"))

    def test_symbol_invalid_empty_string(self):
        self.assertFalse(validate_symbol(""))

    def test_symbol_invalid_with_space(self):
        self.assertFalse(validate_symbol("AAPL "))

    # chart type tests 

    def test_chart_type_valid_bar(self):
        self.assertTrue(validate_chart_type("1"))

    def test_chart_type_valid_line(self):
        self.assertTrue(validate_chart_type("2"))

    def test_chart_type_invalid_zero(self):
        self.assertFalse(validate_chart_type("0"))

    def test_chart_type_invalid_three(self):
        self.assertFalse(validate_chart_type("3"))

    def test_chart_type_invalid_multi_character(self):
        self.assertFalse(validate_chart_type("12"))

    def test_chart_type_invalid_non_numeric(self):
        self.assertFalse(validate_chart_type("a"))

    # time series tests

    def test_time_series_valid_1(self):
        self.assertTrue(validate_time_series("1"))

    def test_time_series_valid_2(self):
        self.assertTrue(validate_time_series("2"))

    def test_time_series_valid_3(self):
        self.assertTrue(validate_time_series("3"))

    def test_time_series_valid_4(self):
        self.assertTrue(validate_time_series("4"))

    def test_time_series_invalid_zero(self):
        self.assertFalse(validate_time_series("0"))

    def test_time_series_invalid_five(self):
        self.assertFalse(validate_time_series("5"))

    def test_time_series_invalid_multi_character(self):
        self.assertFalse(validate_time_series("10"))

    def test_time_series_invalid_non_numeric(self):
        self.assertFalse(validate_time_series("x"))

    # date tests (start/end format)

    def test_date_valid_normal(self):
        self.assertTrue(validate_date("2024-01-15"))

    def test_date_valid_leap_day(self):
        # 2024 is a leap year
        self.assertTrue(validate_date("2024-02-29"))

    def test_date_invalid_bad_format_short_year(self):
        self.assertFalse(validate_date("24-01-15"))

    def test_date_invalid_bad_format_month_day_swapped(self):
        self.assertFalse(validate_date("15-01-2024"))

    def test_date_invalid_wrong_separator(self):
        self.assertFalse(validate_date("2024/01/15"))

    def test_date_invalid_bad_month(self):
        self.assertFalse(validate_date("2024-13-01"))

    def test_date_invalid_bad_day(self):
        self.assertFalse(validate_date("2024-02-30"))

    def test_date_invalid_empty(self):
        self.assertFalse(validate_date(""))

    def test_date_invalid_non_numeric(self):
        self.assertFalse(validate_date("YYYY-MM-DD"))


if __name__ == "__main__":
    unittest.main()
