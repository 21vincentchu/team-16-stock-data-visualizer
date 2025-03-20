import requests
import lxml
import pygal
from datetime import datetime

def main():
    # SHOULD THESE BE SEPARATE FUNCTIONS? - probably yes
    #ask the user to enter the stock symbol for the company they want data for. Should we check with dictionaries to see if that symbol exists
    
    #ask the user for the chart type they would like. (1 or 2), bar or line
    
    #ask the user for the time series function they want the API to use (1,2,3,4)
    
    #ask the user for the beginning date in YYY-MM-DD format
    #ask the user for the end date in YYYY-MM-DD format
        #the end date should not be before the begin datae
        
    symbol=get_symbol()
    dates_tuple = get_date_range()
    start_date = dates_tuple[0]
    end_date = dates_tuple[1]
    
    
    APIdata = get_api_data_with_range(symbol,start_date,end_date)
    print(APIdata)


#*************Main Menu Methods*************# 
#To do: Claire
def get_symbol():
    while True:
        print("\nStock Data Visualizer\n----------------")

        #User enters a symbol
        symbol=input("Enter the stock symbol you are looking for:").strip().upper()
        try:
            #Validate it is a valid symbol
            api_key='W333ESXXCYIWJJS8'
            
            url=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&outputsize=full&apikey={api_key}'
            response=requests.get(url)
            data=response.json()

            if "Global Quote" in data and "01. symbol" in data["Global Quote"]:
                print (f'symbol: {symbol}')
                return symbol
            else:
                print (f'Error: {symbol} not recognized. Try again.')
        except Exception as e:
            print(f"Could not validate symbol. {str(e)}")




#To do: Vinny
def get_chart_type():
    return 1

#to do: Claire
def get_time_series_function():
    #Display options
    while True:
        print('\n Select the Time Series of the chart you want to Generate\n---------------------------------------------------- ')
        print('1. Intraday')
        print('2. Daily')
        print('3. Weekly')
        print('1. Monthly')
    #User inputs choice
        choice= input('Enter time series option (1,2,3,4):')

    #validate choice
        validated_choice= validate_int_input(choice, (1,4))

        if(validated_choice):
            return validated_choice
        else:
            print("Invalid entry")
        




# gathers date range as a string from the user and converts them to datetime objects to be able to date comparisons
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


# method to get results from the alphavantage stock api,
# given symbol, start date, and end date
# IN: symbol,functioNum, start date, end state
# OUT: result with json with the specified start and end dates
def get_api_data_with_range(symbol,functionNum,start_date,end_date):
    api_key = 'W333ESXXCYIWJJS8'

    #dictionary to store the functions needed for options for the chart
    function = {
        1: "TIME_SERIES_INTRADAY",
        2: "TIME_SERIES_DAILY",
        3: "TIME_SERIES_WEEKLY",
        4: "TIME_SERIES_MONTHLY"
    }
    
    api_function = function[functionNum]#sets the number from the parameter into the string function needed for the API call
    symbol = symbol
    url = f'https://www.alphavantage.co/query?function={api_function}&symbol={symbol}&outputsize=full&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    #empty dictionary to store filtered results
    filtered_data = {}
    
    for date_str, values in data['Time Series (Daily)'].items():
        
        #Gets the date of the current json line. turns into a datetime object to compare
        current_date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # If date is in our range, keep it
        if start_date <= current_date <= end_date:
            filtered_data.update({current_date:values})
    
    return filtered_data

def make_chart():
    return 1

 #*************Utility methods*************#  

# function to validate a menu input
# IN: text input from user (string)
# OUT: if input valid, returns numerical result (int)
#      if invalid, returns Null result, which can be evaluated in an if/else statement
def validate_int_input(str_input, range):
    try:
        result = int(str_input)
        if(result>=range[0] && result<=range[1]):
            return result
        else:
            return None
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