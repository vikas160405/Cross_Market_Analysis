import streamlit as st
import pandas as pd

st.title("📊 Cross Market Analysis")

data = {
    "Date": pd.date_range("2025-01-01", periods=5),
    "Bitcoin": [40000, 40500, 41000, 42000, 43000],
    "Oil": [70, 72, 73, 75, 77],
    "S&P 500": [4700, 4720, 4750, 4800, 4850]
}

df = pd.DataFrame(data)

st.metric("Bitcoin Avg", int(df["Bitcoin"].mean()))
st.metric("Oil Avg", int(df["Oil"].mean()))
st.metric("S&P 500 Avg", int(df["S&P 500"].mean()))

st.line_chart(df.set_index("Date"))
st.dataframe(df)
