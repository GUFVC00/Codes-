import numpy as np
import mplfinance as mpf
from datetime import datetime
import yfinance as yf



# Fetch historical stock price data
def fetch_stock_data(ticker_symbol, start_date, end_date):
    return yf.download(ticker_symbol, start=start_date, end=end_date) 

jpm_stock_data = fetch_stock_data('JPM', start_date='2020-01-01', end_date='2024-01-01')

def calculate_historical_volatility(stock_data):
    log_returns = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
    volatility = np.sqrt(252) * log_returns.std()  #252 represent the total days of trading in a year
    return float(volatility)



# Calculate Volatility
jpm_volatility = calculate_historical_volatility(jpm_stock_data)
print(f"JPM Historical Volatility: {jpm_volatility}") 
    