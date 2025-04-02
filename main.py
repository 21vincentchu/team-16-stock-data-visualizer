import requests
import pygal
from datetime import datetime

def main():
    
    #ask the user to enter the stock symbol for the company they want data for
    symbol=get_symbol()
    
    #ask the user for the chart type they would like. (1 or 2), bar or line
    chartType = get_chart_type()

    #ask the user for the time series function they want the API to use (1,2,3,4)
    time_series = get_time_series_function()

    #call date function to get the the beginng and end
    #ask the user for the beginning date in YYY-MM-DD format
    dates_tuple = get_date_range()
    start_date = dates_tuple[0]
    end_date = dates_tuple[1]
    
    #Get the api data
    APIdata = get_api_data_with_range(symbol,time_series,start_date,end_date)
    
    if APIdata:
        # Create and display the chart if we have data
        make_chart(APIdata, chartType, symbol, time_series)
    else:
        print("No data available to create a chart.")


#*************Main Menu Methods*************# 
#To do: Claire
def get_symbol():
    '''
    Function: Get the stock symbol from the user and validate it with the API
    Parameters: None
    Returns: will return nothing, or send a message saying the stock symbol doesn't exist
    '''
    
    while True:
        print("\nStock Data Visualizer\n----------------")

        #User enters a symbol
        symbol=input("Enter the stock symbol you are looking for: ").strip().upper()
        try:
            #Validate it is a valid symbol
            api_key='W333ESXXCYIWJJS8'
            
            url=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&outputsize=full&apikey={api_key}'
            print(url)
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
    '''
    Function: asks user for input, 1 or 2, to get the bar type
    Parameters: none
    Returns: Valid number for the bar type
    '''
    
    while True:
        print("Chart Types\n------------\n1. Bar\n2. Line")
        choice = input("Enter the chart type you want (1,2): ")
    
        validated_choice = validate_int_input(choice,(1,2)) 
        
        if(validated_choice):
            return validated_choice
        else:
            print("Invalid entry")

#to do: Claire
def get_time_series_function():
    '''
    Function: Asks user for time series with a number
    Parameters: None
    Returns: Valid number which corelates to a time series
    '''
    #Display options
    while True:
        print('\n Select the Time Series of the chart you want to Generate\n---------------------------------------------------- ')
        print('1. Intraday, (This will give 5 minute intervals)')
        print('2. Daily')
        print('3. Weekly')
        print('4. Monthly')
    #User inputs choice
        choice= input('Enter time series option (1,2,3,4):')

    #validate choice
        validated_choice= validate_int_input(choice, (1,4))

        if(validated_choice):
            return validated_choice
        else:
            print("Invalid entry")

#to do: Ethan        
def get_date_range():
    '''
    Function: gathers date range as a string from the user and converts them to datetime objects to be able to date comparisons
    Parameters: None
    Returns: Converted Dates (Tuple -> 2 DateTime objects)
    '''
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

#To Do: Vinny
def get_api_data_with_range(symbol, functionNum, start_date, end_date):
    '''
    Function: method to get JSON results from the alphavantage stock api in the specified date range
    Parameters: 
    - symbol: Company symbol ex. IBM
    - functioNum: number corelated to the time series function we want
    - start date: self explanatory 
    - end state: self explanatory
    Returns: result with json with the specified start and end dates 
    '''
    
    api_key = 'W333ESXXCYIWJJS8'

    # Dictionary to map function numbers to API parameters
    function_names = {
        1: "TIME_SERIES_INTRADAY",
        2: "TIME_SERIES_DAILY",
        3: "TIME_SERIES_WEEKLY",
        4: "TIME_SERIES_MONTHLY"
    }
    
    # Get the correct function name
    api_function = function_names[functionNum]
    
    # Build URL based on function type
    if functionNum == 1:  # Special case for intraday
        # For old intraday data, we need month parameter (from docs)
        month_str = start_date.strftime("%Y-%m")
        url = f'https://www.alphavantage.co/query?function={api_function}&symbol={symbol}&interval=5min&month={month_str}&outputsize=full&apikey={api_key}'
    else:
        url = f'https://www.alphavantage.co/query?function={api_function}&symbol={symbol}&outputsize=full&apikey={api_key}'
    
    # Make the request
    response = requests.get(url)
    data = response.json()
    
    # Determine the correct response key
    response_key = ""
    if functionNum == 1:    
        response_key = "Time Series (5min)"
    elif functionNum == 2:
        response_key = "Time Series (Daily)"
    elif functionNum == 3:
        response_key = "Weekly Time Series"
    elif functionNum == 4:
        response_key = "Monthly Time Series"
    
    # Check if we have data
    if response_key not in data:
        print(f"Error: No data available. Response keys: {data.keys()}")
        return {}
    
    # Empty dictionary to store filtered results
    filtered_data = {}
    
    for date_str, values in data[response_key].items():
        try:
            # Parse the date - intraday has time component
            if functionNum == 1:
                current_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            else:
                current_date = datetime.strptime(date_str, "%Y-%m-%d")
            
            # If date is in our range, keep it
            if start_date <= current_date <= end_date:
                filtered_data.update({current_date: values})
                
        except ValueError as e:
            print(f"Error parsing date: {e}")
    
    return filtered_data

#To Do: Vinny
def make_chart(data: dict, chart_type: int, symbol: int, time_series_type: int):
    '''
    Creates and renders a chart based on the stock data.
    
    Parameters:
    - data: Dictionary with datetime objects as keys and stock data as values
    - chart_type: Integer (1 for Bar, 2 for Line)
    - symbol: Stock symbol (string)
    - time_series_type: Integer representing the time series function used
    
    Returns: None (chart opens in browser)
    '''
    
    # Check if we have data
    if not data:
        print("No data available to create chart.")
        return
    
    # Sort the data by date
    sorted_data = dict(sorted(data.items()))
    
    # Convert to lists for pygal
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    
    # Extract data from the values
    for date, values in sorted_data.items():
        date_str = date.strftime('%Y-%m-%d')
        if time_series_type == 1:  # Intraday includes time
            date_str = date.strftime('%Y-%m-%d %H:%M')
        
        dates.append(date_str)
        opens.append(float(values["1. open"]))
        highs.append(float(values["2. high"]))
        lows.append(float(values["3. low"]))
        closes.append(float(values["4. close"]))
    
    # Determine time series name for title
    time_series_names = {
        1: "Intraday (5min)",
        2: "Daily",
        3: "Weekly",
        4: "Monthly"
    }
    time_series_name = time_series_names[time_series_type]
    
    # Create chart based on user choice
    if chart_type == 1:  # Bar Chart
        chart = pygal.Bar(x_label_rotation=45, show_minor_x_labels=False)
    else:  # Line Chart
        chart = pygal.Line(x_label_rotation=45, show_minor_x_labels=False)
        
    # Configure the chart
    chart.title = f'{symbol} Stock Price ({time_series_name})'
    chart.x_labels = dates
    
    # Show only every nth x label to avoid overcrowding
    n = max(1, len(dates) // 20)  # Show at most 20 labels
    chart.x_labels_major = dates[::n]
    
    # Add the data series
    chart.add('Open', opens)
    chart.add('High', highs)
    chart.add('Low', lows)
    chart.add('Close', closes)
    
    # Render the chart in the browser
    chart.render_in_browser()

#*************Utility methods*************#  
#To Do: Ethan
def validate_int_input(str_input, range):
    '''
    Function: to validate a menu input
    Parameters: text input from user (string)
    Returns : if input valid, returns numerical result (int), if invalid, returns Null result
    '''
    
    try:
        result = int(str_input)
        if(result>=range[0] and result<=range[1]):
            return result
        else:
            return None
    except:
        return None
    
#To Do: Ethan
def validate_date_input(str_input):
    '''
    Function: to validate a date input
    Parameters: text input from user (string)
    Returns: if input valid, returns date result (datetime) if invalid, returns Null result
    '''
    
    try:
        result = datetime.strptime(str_input, "%Y-%m-%d")
        return result
    except:
        return None

if __name__ == '__main__':
    main()