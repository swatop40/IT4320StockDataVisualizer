import requests
import json

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
        print(stock_data)
    else:
        print("Failed to retrieve stock data.")

main()