import yfinance as yfin
import streamlit as st
import pandas as pd

# in markdown format below
st.write(
    """
    # Simple stock price app
    
    Shown are the stock closing price and volume of Google
    """
)

# https://towarddatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
ticker = "GOOGL"

# get data on this ticker
tickerData = yfin.Ticker(ticker)

# get the historical prices for this ticker
tickerOf = tickerData.history(period="1d", start="2010-5-31", end="2020-5-31")

# Open    High    Low  Close    Volume  Dividends    Stock  Splits

st.line_chart(tickerOf.Close)
st.line_chart(tickerOf.Volume)
