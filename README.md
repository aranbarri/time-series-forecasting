# 📈 Time Series Forecasting App

A simple app to load time series data, forecast the future using Facebook Prophet, and visualize results with Streamlit.

## 🐳 Run with Docker

```bash
docker-compose up -d
```

Once running, open your browser at [http://localhost:8888](http://localhost:8888)

## 📄 Expected CSV Format

The uploaded CSV file must contain at least:

- `ds`: Date column in YYYY-MM-DD format
- One or more numeric columns to be selected as the target for forecasting

### Example:

```
ds,sales,temperature
2024-01-01,123,15.2
2024-01-02,150,16.8
2024-01-03,170,14.9
```

You will be able to choose which numeric column (e.g., `sales`) to forecast.

## 🔧 Forecast Options

- Select the target column for prediction from your dataset
- Choose how many days to forecast (from 7 to 90 days)
- View results as an interactive time series plot

## 📁 Project Structure

```
time-series-forecasting/
├── app/
│   ├── main.py        # Streamlit app
│   ├── model.py       # Forecasting logic using Prophet
│   └── utils.py       # CSV loading and preprocessing
├── Dockerfile         # Container build instructions
├── docker-compose.yml # Docker service definition
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignored files and folders
└── README.md          # Project documentation
```

## ✅ Features

- Upload your own time series CSV file
- Select a numeric column to forecast
- Adjust forecast length from 7 to 90 days
- Forecast the future using Prophet
- Interactive plot with Streamlit
- Fully containerized with Docker

## 🔧 Technologies

- Python 3.11
- [Prophet](https://facebook.github.io/prophet/)
- [Streamlit](https://streamlit.io/)
- Docker

## 📦 License

MIT License. Feel free to use and adapt.
