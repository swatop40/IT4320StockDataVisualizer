import requests
import json
import pygal

API_KEY = "0W8V2C7EF7NNQ07C"
URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol, function='TIME_SERIES_DAILY', start_date="", end_date=""):
    parameters = {
        "function": function,
        "symbol": symbol,
        "apikey": symbol,
        "datatype": "json"
    }

    if function == "TIME_SERIES_INTRADAY":
        interval = input("Enter the interval (1min, 5min, 15min, 30min, 60min): ")
        parameters["interval"] = interval

    response = requests.get(URL, params=parameters)

    if response.status_code == 200:
        data = response.json()

        if function == "TIME_SERIES_INTRADAY" and "Time Series (1min)" in data:
            return data["Time Series (1min)"]
        elif function == "TIME_SERIES_DAILY" and "Time Series (Daily)" in data:
            return data["Time Series (Daily)"]
        elif function == "TIME_SERIES_WEEKLY" and "Weekly Time Series" in data:
            return data["Weekly Time Series"]
        elif function == "TIME_SERIES_MONTHLY" and "Monthly Time Series" in data:
            return data["Monthly Time Series"]
        else:
            print("Error: Data not available for the given stock symbol or function.")
            return None
    else:
        print("Error: Unable to fetch data from Alpha Vantage.")
        return None

def genBar(stock_data):
    chart_data = {
    "open": [],
    "high": [],
    "low": [],
    "close": []
    }


    for time in sorted(stock_data):
        chart_data["open"].append(float(stock_data[time]["1. open"]))
        chart_data["high"].append(float(stock_data[time]["2. high"]))
        chart_data["low"].append(float(stock_data[time]["3. low"]))
        chart_data["close"].append(float(stock_data[time]["4. close"]))



    BarChart = pygal.Bar()
    BarChart.title = "Test"

    for category, prices in chart_data.items():
        BarChart.add(category, prices)

    BarChart.render_to_file("test.svg")


def genLine(stock_data):

    chart_data = {
    "open": [],
    "high": [],
    "low": [],
    "close": []
    }


    for time in sorted(stock_data):
        chart_data["open"].append(float(stock_data[time]["1. open"]))
        chart_data["high"].append(float(stock_data[time]["2. high"]))
        chart_data["low"].append(float(stock_data[time]["3. low"]))
        chart_data["close"].append(float(stock_data[time]["4. close"]))



    LineChart = pygal.Line()
    LineChart.title = "Test"

    for category, prices in chart_data.items():
        LineChart.add(category, prices)

    LineChart.render_to_file("test.svg")




def main():
    symbol = input("Enter the Stock Symbol: ")
    
    print("Choose a time series function:")
    print("1. DAILY (Time Series Daily)")
    print("2. WEEKLY (Time Series Weekly)")
    print("3. MONTHLY (Time Series Monthly)")
    print("4. INTRADAY (Time Series Intraday)")
    choice = input("Enter the number corresponding to your choice: ")
    
    if choice == "1":
        function = "TIME_SERIES_DAILY"
    elif choice == "2":
        function = "TIME_SERIES_WEEKLY"
    elif choice == "3":
        function = "TIME_SERIES_MONTHLY"
    elif choice == "4":
        function = "TIME_SERIES_INTRADAY"
    else:
        print("Invalid choice. Defaulting to DAILY.")
        function = "TIME_SERIES_DAILY"
    
    stock_data = fetch_stock_data(symbol, function)
    
    if stock_data:
        print(f"Stock data for {symbol} retrieved successfully!")
        while True:
            chartType = input("Would you like your data in a Bar Graph or Line Graph?(enter 1 or 2 respectively) ")
            if chartType == "1":
                genBar(stock_data)
                break
            elif chartType =="2":
                genLine(stock_data)
                break
            elif chartType != "1" or "2":
                print("Please enter 1 to generate a Bar Graph or 2 to generate a Line Graph")


    else:
        print("Failed to retrieve stock data.")

main()