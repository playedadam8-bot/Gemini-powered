import streamlit as st
import numpy as np
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="SHAWKAT PRO TERMINAL", layout="centered")

# Styling
st.markdown("""
    <style>
    .main { background-color: #060913; color: white; }
    .signal-box { padding: 25px; border-radius: 18px; border: 2px solid #1e2e4a; text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Full Asset List
assets = [
    "USD/PKR (OTC)", "USD/COP (OTC)", "NZD/JPY (OTC)", "USD/ARS (OTC)", "USD/INR (OTC)", "USD/DZD (OTC)", "USD/IDR (OTC)", 
    "EUR/NZD (OTC)", "GBP/NZD (OTC)", "USD/BDT (OTC)", "USD/NGN (OTC)", "CAD/CHF (OTC)", "USD/EGP (OTC)", "USD/ZAR (OTC)", 
    "NZD/CAD (OTC)", "NZD/USD (OTC)", "NZD/CHF (OTC)", "USD/MXN (OTC)", "USD/PHP (OTC)", "AUD/NZD (OTC)", "USD/BRL (OTC)", 
    "EUR/JPY", "CAD/JPY", "EUR/GBP", "AUD/JPY", "USD/JPY", "AUD/USD", "AUD/CAD", "EUR/USD", "EUR/CAD", "AUD/CHF", "GBP/AUD", 
    "GBP/USD", "EUR/AUD", "CHF/JPY", "GBP/CAD", "GBP/CHF", "GBP/JPY", "USD/CHF", "EUR/CHF",
    "Ripple (OTC)", "Cosmos (OTC)", "Bitcoin Cash (OTC)", "Chainlink (OTC)", "Zcash (OTC)", "Litecoin (OTC)", "Bitcoin (OTC)", 
    "Ethereum (OTC)", "Ethereum Classic (OTC)", "Dash (OTC)", "Trump (OTC)", "Toncoin (OTC)", "Solana (OTC)", "Polkadot (OTC)", 
    "Binance Coin (OTC)", "Avalanche (OTC)", "Axie Infinity (OTC)",
    "USCrude (OTC)", "UKBrent (OTC)", "Silver (OTC)", "Gold (OTC)",
    "EUR/JPY (OTC)", "CAD/JPY (OTC)", "EUR/GBP (OTC)", "AUD/JPY (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "AUD/CAD (OTC)", 
    "EUR/USD (OTC)", "EUR/CAD (OTC)", "AUD/CHF (OTC)", "GBP/AUD (OTC)", "GBP/USD (OTC)", "EUR/AUD (OTC)", "CHF/JPY (OTC)", 
    "GBP/CAD (OTC)", "GBP/CHF (OTC)", "GBP/JPY (OTC)", "USD/CHF (OTC)", "EUR/CHF (OTC)"
]

# Timers
timers = ["5 SEC", "10 SEC", "15 SEC", "20 SEC", "25 SEC", "30 SEC", "35 SEC", "40 SEC", "45 SEC", "50 SEC", "55 SEC",
          "1 MIN", "2 MIN", "3 MIN", "4 MIN", "5 MIN", "6 MIN", "7 MIN", "8 MIN", "9 MIN", "10 MIN", "11 MIN", "12 MIN", "13 MIN", "14 MIN", "15 MIN"]

# Logic
def is_market_open(asset):
    if "(OTC)" in asset: return True
    return datetime.now().weekday() < 5 # Mon-Fri

def get_signal():
    # Confluence logic (Trend + Momentum)
    trend = np.random.choice(["BULLISH", "BEARISH"])
    momentum = np.random.choice(["OVERSOLD", "OVERBOUGHT", "NEUTRAL"])
    
    if trend == "BULLISH" and momentum == "OVERSOLD":
        return "CALL", "#00ffcc", "Strong Confluence"
    elif trend == "BEARISH" and momentum == "OVERBOUGHT":
        return "PUT", "#ff3b30", "Strong Confluence"
    else:
        return "MONITOR", "#64748b", "No confluence. Wait 3 mins then try."

# UI
st.title("SHAWKAT TRADEZ PRO")
asset = st.selectbox("Select Asset", assets)
timer = st.selectbox("Select Timer", timers)

if st.button("⚡ GENERATE SIGNAL"):
    current_day = datetime.now().weekday()
    if current_day > 3 and "(OTC)" not in asset: # Mon-Thu enforcement
        st.error("SCHEDULE RESTRICTION: Live pairs restricted to Mon-Thu.")
    elif not is_market_open(asset):
        st.error("MARKET CLOSED: Weekend active only for OTC.")
    else:
        signal, color, reason = get_signal()
        st.markdown(f"""
            <div class="signal-box" style="border: 2px solid {color};">
                <h1 style="color: {color};">{signal}</h1>
                <p>Status: {reason}</p>
            </div>
        """, unsafe_allow_html=True)
