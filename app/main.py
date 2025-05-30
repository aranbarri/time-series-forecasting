import streamlit as st
from model import forecast
from utils import load_data
import pandas as pd

st.title("Time Series Forecasting App")

uploaded_file = st.file_uploader("Upload your CSV file (must contain a 'ds' column for dates)", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("Data preview")
    st.dataframe(df.head())

    # Valid target columns (exclude 'ds' and non-numeric)
    possible_targets = [col for col in df.columns if col != "ds" and df[col].dtype != 'O']
    if not possible_targets:
        st.error("No valid numeric columns found besides 'ds'.")
    else:
        target_col = st.selectbox("Select the column to forecast:", possible_targets)
        n_days = st.slider("Select number of days to forecast", min_value=5, max_value=90, value=30)

        df_prepped = df[["ds", target_col]].rename(columns={target_col: "y"})
        future, forecast_df = forecast(df_prepped, n_days)

        # Show only forecast data after the last date in original dataset
        last_date = df_prepped["ds"].max()
        forecast_only = forecast_df[forecast_df["ds"] > last_date]

        st.subheader(f"Forecast (next {n_days} days from {last_date.date() + pd.Timedelta(days=1)})")
        st.line_chart(forecast_only.set_index("ds")[["yhat", "yhat_lower", "yhat_upper"]])
