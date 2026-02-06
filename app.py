import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cross Market Analysis", layout="wide")

# ---------------- DATA ----------------
@st.cache_data
def load_data():
    dates = pd.date_range("2025-01-01", periods=10)

    crypto = pd.DataFrame({
        "date": dates,
        "bitcoin_price": [40000, 40200, 39800, 40500, 41000, 41500, 42000, 41800, 42500, 43000]
    })

    oil = pd.DataFrame({
        "date": dates,
        "oil_price": [70, 71, 69, 72, 73, 74, 75, 74, 76, 77]
    })

    stock = pd.DataFrame({
        "date": dates,
        "sp500_close": [4700, 4720, 4690, 4715, 4750, 4780, 4800, 4790, 4820, 4850]
    })

    df = crypto.merge(oil, on="date").merge(stock, on="date")
    return df

df = load_data()

# ---------------- UI ----------------
st.title("📊 Cross-Market Analysis")

col1, col2, col3 = st.columns(3)
col1.metric("Bitcoin Avg Price", round(df["bitcoin_price"].mean(), 2))
col2.metric("Oil Avg Price", round(df["oil_price"].mean(), 2))
col3.metric("S&P 500 Avg Close", round(df["sp500_close"].mean(), 2))

st.line_chart(df.set_index("date"))
st.dataframe(df)
