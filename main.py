import requests
import lxml
import pygal
from datetime import datetime

def main():
    # SHOULD THESE BE SEPARATE FUNCTIONS?
    #ask the user to enter the stock suymbol for the company they want data for
    #ask the user for the chart type they would ike
    #ask the user for the time series function they want the API to use
    
    #ask the user for the beginning date in YYY-MM-DD format
    #ask the user for the end date in YYYY-MM-DD format
        #the end date should not be before the begin datae
    dates_tuple = get_date_range()
    start_date = dates_tuple[0]
    end_date = dates_tuple[1]


    #API key = W333ESXXCYIWJJS8
    #generate a graph and open in the user's default browser
    #function API parameter and then Symbol
    function="TIME_SERIES_DAILY"
    symbol="IBM"
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey='

    


######********************
###### Main Menu Methods


# gathers date range and converts them to datetime objects
# IN: None
# OUT: Converted Dates (Tuple -> 2 DateTime objects)
def get_date_range():
    while True:
        # collect inputs
        start_date_str = input("Enter the start Date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end Date (YYYY-MM-DD): ")
        # attempt to convert to date type
        start_date = validate_date_input(start_date_str)
        end_date = validate_date_input(end_date_str)
        # check conversion worked
        if(start_date and end_date):
            # validate begin date is before end date
            if(start_date > end_date): # if start date is later than end date
                print("\nError: Please ensure the start date is before the end date")
                continue

            # otherwise return converted datetime objects in a tuple
            return (start_date, end_date)
        else:
            print("\nError: Please enter valid date.\n\n")
            continue






######********************
###### Utility Methods

# method to get results from the alphavantage stock api,
# given a url with the applied settings passed.
# IN: url excluding api key (string)
# OUT: result (json)
def get_api_data(url):
    api_key = 'W333ESXXCYIWJJS8'
    final_url= f"{url}{api_key}"
    response = requests.get(final_url)
    result = response.json()
    return result

# function to validate a menu input
# IN: text input from user (string)
# OUT: if input valid, returns numerical result (int)
#      if invalid, returns Null result, which can be evaluated in an if/else statement
def validate_int_input(str_input):
    try:
        result = int(str_input)
        return result
    except:
        return None

# function to validate a date input
# IN: text input from user (string)
# OUT: if input valid, returns date result (datetime)
#      if invalid, returns Null result, which can be evaluated in an if/else statement
def validate_date_input(str_input):
    try:
        result = datetime.strptime(str_input, "%Y-%m-%d")
        return result
    except:
        return None



if __name__ == '__main__':
    main()