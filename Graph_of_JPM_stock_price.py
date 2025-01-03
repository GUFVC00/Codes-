import yfinance as yf
import matplotlib.pyplot as plt

import mplfinance as mpf
import plotly.graph_objects as go
from datetime import datetime



# Fetch historical stock price data
def fetch_stock_data(ticker_symbol, start_date, end_date):
    return yf.download(ticker_symbol, start=start_date, end=end_date) 

jpm_stock_data = fetch_stock_data('JPM', start_date='2020-01-01', end_date='2024-01-01')

plt.figure(figsize=(10, 5))
plt.plot(jpm_stock_data['Close'], label="JPM Close Price")
plt.title('JPM Historical Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()