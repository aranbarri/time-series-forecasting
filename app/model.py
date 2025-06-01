from prophet import Prophet

def forecast(df, periods=30):
    # Ensure dataframe has 'ds' and 'y' columns
    df = df.copy()
    if 'y' not in df.columns:
        df.columns = ['ds', 'y'] + df.columns.tolist()[2:]

    # Initialize Prophet with advanced settings
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        seasonality_mode='multiplicative',
        changepoint_prior_scale=0.05,
        seasonality_prior_scale=10.0
    )

    # Fit the model
    model.fit(df)

    # Create future dataframe
    future = model.make_future_dataframe(periods=periods)

    # Generate forecast
    forecast = model.predict(future)
    return future, forecast
