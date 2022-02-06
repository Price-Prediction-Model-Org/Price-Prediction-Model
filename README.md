# Price-Prediction-Model

This project’s goal is to develop a machine learning model that can predict a cryptocurrency's future market price. 

A LSTM model is trained on historical price data that is pulled in through an API and stored in a relational database. 

The model attempts to predict prices for a chosen time window, for both Bitcoin and Ethereum.

Our app is deployed using Heroku:

https://price-prediction-model.herokuapp.com/

<hr>
# Dataset:
The daily crypto price data has been pulled in through an API on CryptoCompare:

https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistoday

The pricing information includes: timestamp, high, low, open, volumefrom, volumeto, and close. We will most likely save all the data, but only use one of the pricing metrics to train the model.
<hr>
# ETL proccess
The API data includes timestamp, high, low, open, volumefrom, volumeto, and close. in addition to these columns, we've created a coin, 
<hr>
# Data storage
* We used Heroku Postgres to store data for our app.
* The database updates only when needed, based on the current and last unix timestamp in the db
Database updates up to once daily, when index page loads, based on 00:00 GMT time zone.
* Time units were daily only.
* Data for both coins was stored in 1 table, due to limitations of a free Heroku Postgres database.
<hr>
# Long Short Term Memory (LSTM) Model
  The Long Short Term Model (LSTM) has been used to do the price forecasting. LSTM is a slightly more sophisticated version of a Recurrent Neural Network (RNN) which incorporates long term memory. The model will be trained on historical price data and used to predict the next value in the series. (Time window for predictions, tbd)
<hr>
# Visualization
HTML/CSS/Plotly has been used to do the visualization and plots.
Here are the final plots and Welcome page:

**Welcome Page:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Marquee.png" height="450" width="600" >
<hr>
**Bitcoin PricePerformance Plot and Table:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Bitcoin%20Price%20Performance%20plot.png" height="450" width="600" >
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinTable.png)" height="450" width="600" >

<hr>
**Bitcoin Candlestick chart:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinCandlestickPlot.png" height="450" width="600" >
<hr>
**Bitcoin Price Prediction Model:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinPricePredictionPlot.png" height="450" width="600" >
<hr>

**Bitcoin Price Acceleration Plot:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinPriceAccelerationPlot.png" height="450" width="600" >
<hr>

**Ethereum Price Performance Plot and Table:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/EthereumPricePerformancePlot.png" height="450" width="600" >
<hr>
**Ethereum Candlestick Plot:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Ethereum%20CandlestickPlot.png" height="450" width="600" >
<hr>
**Bitcoin vs Ethereum Comparison Table and Plot:**
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinEthereumComparisonTable.png" height="450" width="600" >
<br>
<img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinEthereumComparisonPlot.png" height="450" width="600" >
<hr>

# Team Members:
    Anna Weeks
    Hima Vissa
    Jacob Trevithick
    Lekshmi Prabha
  <hr>















