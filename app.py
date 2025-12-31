import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Data Analyzer", layout="wide")

st.title("📚 Web Scraping & Data Analysis App")

df = pd.read_csv("books_cleaned.csv")

st.metric("Total Books", df.shape[0])
st.metric("Average Price (£)", round(df["Price"].mean(), 2))
st.metric("Average Rating", round(df["Rating"].mean(), 2))

st.dataframe(df)

st.bar_chart(df["Rating"].value_counts())

st.download_button(
    "Download Cleaned Data",
    df.to_csv(index=False),
    "books_cleaned.csv"
)
