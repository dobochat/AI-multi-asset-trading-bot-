import streamlit as st
import os
from trading_engine import run_trading_engine

st.set_page_config(page_title="AI Multi-Asset Trading Bot", layout="centered")
st.title("🚀 AI Trading Bot - NSE/BSE/Options")

mode = os.getenv("TRADING_MODE", "paper")
st.markdown(f"**Trading Mode:** `{mode.upper()}`")

symbol = st.text_input("Enter Trading Symbol (e.g., RELIANCE, NIFTY24JUL23000CE):")
quantity = st.number_input("Enter Quantity:", min_value=1, value=1, step=1)

if st.button("Start Trade"):
    if symbol and quantity > 0:
        logs = run_trading_engine(mode, symbol, quantity)
        for log in logs:
            st.write(log)
    else:
        st.warning("Please enter valid symbol and quantity.")