import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from streamlit_autorefresh import st_autorefresh

import Live_pricetracker as lp
import index_data as id
# Create a Streamlit app
st.title("Stock Dashboard")

# Define index tickers
index_tickers = ["NSEI", "NIFTY BANK", "SENSEX"]

# Create a dropdown for index selection
#selected_index = st.selectbox("Select Index", index_tickers)

# Fetch and display index data
index_data = id.get_index_data(index_tickers[0])
chart_container = st.container()

with chart_container:
    st.line_chart(index_data['Close'], height=200, width=300)


# Create a text input for stock selection
stock_ticker = st.text_input("Enter Stock Ticker")

# Fetch and display stock data
if stock_ticker:
    stock_data =yf.download(stock_ticker+".NS", period="max") 
    #st.line_chart(stock_data)

    # Create tabs for different timeframes
    tabs = st.tabs(["1m", "3m", "6m", "1y","1D"])

    with tabs[0]:
        st.line_chart(stock_data['Close'].tail(30))

    with tabs[1]:
        st.line_chart(stock_data['Close'].tail(90))

    with tabs[2]:
        st.line_chart(stock_data['Close'].tail(180))

    with tabs[3]:
        st.line_chart(stock_data['Close'].tail(365))

    with tabs[4]:
        # Use st_autorefresh to update the chart every 10 seconds
        st_autorefresh(key="live_price_chart")
        live_price_data = lp.get_stock_price(stock_ticker)
        st.line_chart(live_price_data)