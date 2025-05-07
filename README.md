# Amazon Stock Price Prediction

<h4>Project contributor :</h4>

* [ MITHUN S](https://github.com/ST-MITHUN) <br/>

The project uses Facebook Prophet, which is a powerful library for time-series forecasting. It automatically detects seasonal patterns, holidays, and trends in the data, providing a reliable prediction of future stock prices.

This uses Facebook Prophet Machine learning model in order to forecast the price of Amazon 30 days into the future. We have utilised plotly express for data visualization and evaluated the forecast using google finance in google sheets. Further, we have automated the entire stock forecasting process, enabling instantaneous forecast for any preferred stock.


📌 Key Functions in the Code

* load_data(): Loads historical stock data.

* preprocess_data(): Cleans and prepares data for modeling.

* train_model(): Trains the Facebook Prophet model.

* forecast_future(): Predicts future stock prices for a specified period.

* plot_forecast(): Visualizes the forecasted results with interactive plots.

* save_forecast(): Exports predictions to a CSV file.


🔍 Results

* The model outputs:

* Future Stock Prices: A detailed forecast of the stock price.

* Interactive Graphs: Visualization of predictions.

* CSV Export: Future predictions are saved in forecast_updated.csv.

🌐 Technologies Used

*   Python 🐍

*   Facebook Prophet 🔮

*   Plotly 📊

*   Pandas 🗃️

*   Jupyter Notebook 📓

🛠️ Future Enhancements

* Real-time data fetching using APIs.

* Integration with Machine Learning for better prediction.

* Enhanced visualization for deeper analysis.


Created Facebook Prophet Model

```bash
from prophet import Prophet
m = Prophet()
m.fit(prophet_df)

```
Forecasting

```bash
 future=m.make_future_dataframe(periods=30)
forecast=m.predict(future)
forecast     
```
Using Plotly for data visualization
```bash
px.line(forecast, x='ds', y='yhat')
figure=m.plot(forecast,xlabel='ds',ylabel='y')
figure2=m.plot_components(forecast)
```
Downloading Forecasted Data
```bash
from google.colab import files
forecast.to_csv('forecast.csv')
files.download('forecast.csv')
```
ScreenShots:

![image](https://github.com/user-attachments/assets/2196a304-9379-49aa-ad8c-7f5c9452c654)



![image](https://github.com/user-attachments/assets/5c5abd50-d5d0-491a-b7d9-4c79035e0be4)

