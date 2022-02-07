import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Bongo's Stock Tracker")
st.write(''' 
Just a simple stock price tracker will probably add more shit to it 

''')


st.sidebar.title('Pick your stock')
ticker = st.sidebar.text_input('Enter stock ticker')



sd = st.sidebar.date_input('Start Date')
se = st.sidebar.date_input('End Date')

ticker_data = yf.Ticker(ticker)
ticker_df = ticker_data.history(period = '2d', start = sd, end= se )

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)





# Let's see what we got!

