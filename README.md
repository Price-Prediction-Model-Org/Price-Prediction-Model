# Price-Prediction-Model

This project’s goal is to develop a machine learning model that can predict a cryptocurrency's future market price. 

A LSTM model is trained on historical price data that is pulled in through an API and stored in a relational database. 

The model attempts to predict prices for a chosen time window, for both Bitcoin and Ethereum.

Our app is deployed using Heroku:

https://price-prediction-model.herokuapp.com/


# Dataset:
The daily crypto price data has been pulled in through an API on CryptoCompare:

https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistoday

The pricing information includes: timestamp, high, low, open, volumefrom, volumeto, and close. We will most likely save all the data, but only use one of the pricing metrics to train the model.

# ETL proccess
The API data includes timestamp, high, low, open, volumefrom, volumeto, and close. in addition to these columns, we've created a coin, 

# Data storage
* We used Heroku Postgres to store data for our app.
* The database updates only when needed, based on the current and last unix timestamp in the db
Database updates up to once daily, when index page loads, based on 00:00 GMT time zone.
* Time units were daily only.
* Data for both coins was stored in 1 table, due to limitations of a free Heroku Postgres database.

# Long Short Term Memory (LSTM) Model
  The Long Short Term Model (LSTM) has been used to do the price forecasting. LSTM is a slightly more sophisticated version of a Recurrent Neural Network (RNN) which incorporates long term memory. The model will be trained on historical price data and used to predict the next value in the series. (Time window for predictions, tbd)

# Visualization
HTML/CSS/Plotly has been used to do the visualization and plots.
Here are the final plots and Welcome page:

**Welcome Page:**
<a href="url"><img src="https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Marquee.png" height="48" width="48" ></a>
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Marquee.png){:height="36px" width="36px"}

**Bitcoin PricePerformance Plot and Table:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Bitcoin%20Price%20Performance%20plot.png)
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinTable.png)

**Bitcoin Candlestick chart:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinCandlestickPlot.png)

**Bitcoin Price Prediction Model:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinPricePredictionPlot.png)

**Bitcoin Price Acceleration Plot:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinPriceAccelerationPlot.png)


**Ethereum Price Performance Plot and Table:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/EthereumPricePerformancePlot.png)


**Ethereum Candlestick Plot:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/Ethereum%20CandlestickPlot.png)

**Bitcoin vs Ethereum Comparison Table and Plot:**
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinEthereumComparisonTable.png)
![](https://github.com/Price-Prediction-Model-Org/Price-Prediction-Model-Group/blob/main/images/BitcoinEthereumComparisonPlot.png)

# Team Members:
    Anna Weeks
    Hima Vissa
    Jacob Trevithick
    Lekshmi Prabha















