import unittest
from unittest.mock import patch
from datetime import datetime
from main import validate_date_input, validate_int_input
from main import get_symbol, get_chart_type, get_time_series_function, get_date_range
'''
What is patch? https://realpython.com/python-mock-library/
'''

class TestGetDateRange(unittest.TestCase):
    def test_valid_input(self):
        # Simulate user typing two valid dates
        user_inputs = ['2024-01-01', '2024-12-31']

        #Patch replaces user input, and uses whatevers in the "user_input" variable
        #patch is the "input robot"
        #side_effect = the input we feed 
        with patch('builtins.input', side_effect=user_inputs):
            start, end = get_date_range()

            #compares whats in start and end, with the dates we give it
            self.assertEqual(start, datetime(2024, 1, 1))
            self.assertEqual(end, datetime(2024, 12, 31))
    
    def test_valid_date(self):
        # Test a correct date
        date_str = '2024-04-22'
        expected_result = datetime(2024, 4, 22)
        self.assertEqual(validate_date_input(date_str), expected_result)

    def test_invalid_date(self):
        # Test an incorrect date
        date_str = 'not-a-date'
        self.assertIsNone(validate_date_input(date_str))

    def test_wrong_format_date(self):
        # Test a wrong format (should be YYYY-MM-DD)
        date_str = '04/22/2024'
        self.assertIsNone(validate_date_input(date_str))

    def test_empty_string(self):
        # Test empty string input
        date_str = ''
        self.assertIsNone(validate_date_input(date_str))
            

if __name__ == '__main__':
    unittest.main()