import pandas as pd

def load_data(file):
    # Read CSV and ensure 'ds' is datetime
    df = pd.read_csv(file)
    df['ds'] = pd.to_datetime(df['ds'])
    return df
