import unittest
from unittest.mock import patch
from datetime import datetime
from main import validate_date_input, validate_int_input
from main import get_symbol, get_chart_type, get_time_series_function, get_date_range

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

class TestGetTimeSeries(unittest.TestCase):
    def test_valid_input(self):
        # define user inputs
        user_input = '2'
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_time_series_function()
            # compare result to expected correct result
            self.assertEqual(2, result)
        
    def test_out_of_range_input(self):
        # define user inputs
        user_input = '8' # this number is beyond the max range of the input, which is 4
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_time_series_function()
            # compare result to expected correct result
            self.assertIsNone(result)
    
    def test_invalid_input(self):
        # define user inputs
        user_input = 'a'
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_time_series_function()
            # compare result to expected correct result
            self.assertIsNone(result)

    def test_empty_input(self):
        # define user inputs
        user_input = '' 
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_time_series_function()
            # compare result to expected correct result
            self.assertIsNone(result)

class TestGetChartType(unittest.TestCase):
    def test_valid_input(self):
        # define user inputs
        user_input = '2'
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_chart_type()
            # compare result to expected correct result
            self.assertEqual(2, result)
        
    def test_out_of_range_input(self):
        # define user inputs
        user_input = '3' # this number is beyond the max range of the input, which is 2
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_chart_type()
            # compare result to expected correct result
            self.assertIsNone(result)
    
    def test_invalid_input(self):
        # define user inputs
        user_input = 'a'
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_chart_type()
            # compare result to expected correct result
            self.assertIsNone(result)

    def test_empty_input(self):
        # define user inputs
        user_input = '' 
        # use patch to execute function
        with patch('builtins.input', side_effect=user_input):
            result = get_chart_type()
            # compare result to expected correct result
            self.assertIsNone(result)

class TestGetSymbol(unittest.TestCase):

    #valid stock symbol
    def test_valid_symbol(self):
        user_input=['AAPL']

        with patch('builtins.input', side_effect=user_input):
            symbol=get_symbol()
            self.assertEqual(symbol,'AAPl')
    
    #tests when user enters empty string then a symbol
    def test_empty_symbol(self):
        user_inputs=['','AAPl']

        with patch('builtins.input', side_effect=user_inputs):
            symbol=get_symbol()
            self.assertEqual(symbol,'AAPl')
    
    #lowercase converted to uppercase
    def test_lowercase_symbol(self):
        user_inputs=['aapl']

        with patch('builtins.input', side_effect=user_inputs):
            symbol=get_symbol()
            self.assertEqual(symbol,'AAPl')


if __name__ == '__main__':
    unittest.main()