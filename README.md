📊 Cross Market Analysis Dashboard

An interactive financial data dashboard that compares multiple markets including Cryptocurrency, Crude Oil, and Stock Market indices in one place using Python and Streamlit.

The project collects data from different sources, processes it, stores it in a SQLite database, and visualizes it using an interactive Streamlit web application.

🚀 Project Features
📈 Market Overview

Compare Bitcoin, Oil, and S&P 500 prices

View average price metrics

Filter data using date range

📊 SQL Query Runner

Run predefined SQL queries on the database

Example queries include:

Top cryptocurrencies

Oil average prices

Highest NASDAQ closing price

🪙 Crypto Price Trend

Select cryptocurrencies such as Bitcoin, Ethereum, and Tether

Choose a date range

View historical price trends using charts

🛠️ Technologies Used

Python

Streamlit

SQLite

Pandas

yFinance

CoinGecko API

Jupyter Notebook

🌐 Data Sources

The project collects financial data from the following sources:

CoinGecko API → Cryptocurrency data

Yahoo Finance (yFinance) → Stock market data

GitHub CSV Dataset → WTI Crude Oil price data

🗄️ Database Structure

The project uses a SQLite database (cross_market.db) containing the following tables:

cryptocurrencies

crypto_prices

oil_prices

stock_prices

These tables store historical and market data for analysis.

🔄 Data Pipeline

Data is fetched from CoinGecko API, Yahoo Finance, and GitHub datasets

Jupyter Notebook processes and cleans the data

The processed data is stored in SQLite database

The Streamlit dashboard reads the data and displays visualizations

🏗️ Architecture

Data Sources
⬇
Jupyter Notebook (Fetch → Clean → Transform → Store)
⬇
SQLite Database
⬇
Streamlit Dashboard

📊 Project Presentation

You can view the full project presentation here:

🔗 Project PPT (PDF)
https://drive.google.com/file/d/1l3XUCcQKtA21Z8iWj1RX8z0agWteYc18/view?usp=sharing

📌 Conclusion

This project demonstrates how multi-asset financial data can be collected, stored, analyzed, and visualized using Python and Streamlit, helping users compare trends across cryptocurrency, oil, and stock markets.
