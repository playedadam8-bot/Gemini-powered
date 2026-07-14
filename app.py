import streamlit as st
import numpy as np
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="SHAWKAT TRADEZ PRO", layout="centered")

# 2. Styling
st.markdown("""
    <style>
    .main { background-color: #060913; color: white; }
    .signal-box { padding: 25px; border-radius: 18px; border: 2px solid #1e2e4a; text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# 3. Market Logic
def is_market_open(asset):
    # OTC assets are available 24/7
    if "(OTC)" in asset:
        return True
    # Live assets (no OTC suffix) are closed on weekends (5=Sat, 6=Sun)
    current_day = datetime.now().weekday()
    return current_day < 5

# 4. Strategy Engine (Triple Confluence)
def get_pro_signal():
    # Simulated Confluence Logic
    trend = np.random.choice(["BULLISH", "BEARISH"])
    momentum = np.random.choice(["OVERSOLD", "OVERBOUGHT", "NEUTRAL"])
    volatility = np.random.choice(["HIGH", "LOW"])
    
    if trend == "BULLISH" and momentum == "OVERSOLD" and volatility == "HIGH":
        return "STRONG CALL", "#00ffcc", "Triple Confluence: Trend + Momentum + Volatility"
    elif trend == "BEARISH" and momentum == "OVERBOUGHT" and volatility == "HIGH":
        return "STRONG PUT", "#ff3b30", "Triple Confluence: Trend + Momentum + Volatility"
    else:
        return "WAIT", "#64748b", "Insufficient Market Confluence"

# 5. Interface
st.title("SHAWKAT TRADEZ PRO")

# Comprehensive Asset List
assets = [
    "EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "AUD/USD", "USD/CAD", "NZD/USD", # Major Forex
    "EUR/GBP", "EUR/JPY", "EUR/CHF", # Cross Pairs
    "Gold (OTC)", "Bitcoin (OTC)", "Ethereum (OTC)", "USCrude (OTC)", # Popular OTC
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/JPY (OTC)"
]

asset = st.selectbox("Select Asset", assets)
timer = st.selectbox("Timer", ["1 MIN", "2 MIN", "5 MIN", "15 MIN"])

if st.button("⚡ GENERATE PRO SIGNAL"):
    if not is_market_open(asset):
        st.error("MARKET CLOSED: This live asset is unavailable on weekends.")
    else:
        signal, color, reason = get_pro_signal()
        st.markdown(f"""
            <div class="signal-box" style="border-color: {color};">
                <h1 style="color: {color};">{signal}</h1>
                <p>Status: {reason}</p>
            </div>
        """, unsafe_allow_html=True)
