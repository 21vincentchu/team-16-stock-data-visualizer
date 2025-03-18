import requests
import lxml
import pygal

def main():
    print("hello")

    #ask the user to enter the stock suymbol for the company they want data for
    #ask the user for the chart type they would ike
    #ask the user for the time series function they want the API to use
    #ask the user for the beginning date in YYY-MM-DD format
    #ask the user for the end date in YYYY-MM-DD format
        #the end date should not be before the begin datae


    #API key = W333ESXXCYIWJJS8
    #generate a graph and open in the user's default browser
    #function API parameter and then Symbol
    function="TIME_SERIES_DAILY"
    symbol="IBM"
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=W333ESXXCYIWJJS8'
    r = requests.get(url)
    data = r.json()

    print(data)


if __name__ == '__main__':
    main()