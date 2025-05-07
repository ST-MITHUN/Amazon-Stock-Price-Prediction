import pandas as pd
from prophet import Prophet
'from fbprophet import Prophet'
import matplotlib.pyplot as plt
import logging

# To suppress the info logs
logging.getLogger('cmdstanpy').setLevel(logging.WARNING)

# Step 1: Load the data
file_path = 'AMZN.csv'
df = pd.read_csv(file_path)

# Step 2: Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Close']]
df.columns = ['ds', 'y']

# Step 3: Initialize and Fit the Model
model = Prophet(daily_seasonality=True)
model.fit(df)

# Step 4: Make Predictions
future = model.make_future_dataframe(periods=30)  # Predicting for the next 30 days
forecast = model.predict(future)

# Save the forecast for evaluation
forecast.to_csv('forecast_updated.csv', index=False)


# Step 5: Plotting
fig1 = model.plot(forecast)
plt.title("Amazon Stock Price Forecast (Next 30 Days)")
plt.xlabel("Date")
plt.ylabel("Stock Price ($)")
plt.show()

fig2 = model.plot_components(forecast)
plt.show()

"/mnt/data/forecast_updated.csv"
