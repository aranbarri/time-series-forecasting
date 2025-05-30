from prophet import Prophet

def forecast(df, periods=30):
    # Initialize and train the model
    model = Prophet()
    model.fit(df)

    # Create a DataFrame for future dates
    future = model.make_future_dataframe(periods=periods)

    # Generate forecast
    forecast = model.predict(future)
    return future, forecast
