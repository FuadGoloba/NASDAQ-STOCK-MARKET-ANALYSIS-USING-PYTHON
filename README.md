# NASDAQ-STOCK-MARKET-ANALYSIS-USING-PYTHON
Authors: Fuad Goloba
         Darshan Amin
         Alp Ates

Program Overview
This project is a financial analytics project developed by my team (3 individuals) in the first semester of my master’s program in Business Analytics. The project was designed to allow advanced Business Analysts without programming knowledge to consult, analyse, and model stock time series. Descriptive and Predictive analytics were utilized to  provide the possibility of searching  for specific stocks, and querying specified time ranges along with associated analysis, such as statistical descriptions of prices and/or volume (mean, median, range, etc), technical indicators, visualisation (of the raw data, but also of transformations, such as moving averages), and even basic modelling (such as regression) as users can employ the program to predict future prices of various companies’ stocks to better decide what stocks to trade within a range of period.

Data Gathering
The program sources stock data of a list of active trading companies from 1970 online from NASDAQ but also optimises the use of downloaded data to avoid excessive network.

System Requirements
•	Windows Operating System / Mac Os
•	Python 3 or higher versions
•	Internet connection for real time data
 
Getting started

Before running program:
1.	Make sure you have Python 3.0 or higher version installed in your computer (Windows/Mac).
2.	Install below packages in CMD (Windows) or Terminal (Mac):
a.	Install pandas_datareader package by using following command: - pip install pandas_datareader
b.	Install pmdarima package by using following command: - pip install pmdarima
c.	Install mpl_finance package by using following command: - pip install mpl_finance
3.	Make user to save stock_market.py program and the related modules in same folder on your computer.

Executing the program:

1.	For Windows and Mac users open the directory where the file has been saved in CMD or Terminal and type python stock_market.py to execute the program.
2.	You will get two options:
a.	Update Nasdaq Company symbol list on the computer if you this that a new company has been publicly announced in Nasdaq recently.
b.	Select the company for which you want to analyse the stock by providing company symbol as input.
3.	Once you have selected the company you will get the options to perform descriptive analysis or predictive analysis or select a new company.
Descriptive Analysis:
On selecting descriptive analysis, you will be given two options as below:
1.	Checking the descriptive numerical statistics:
Enter the from date and to date in format of (DD/MM/YYYY) for the duration you want to retrieve numerical statistics: Percentage gain, mean, maximum, range, quartiles, standard deviation and coefficient of variance for closing share price of the company you selected.
2.	Visualising the historical stock data:
Enter the from date and to date in format of (DD/MM/YYYY) for the duration you want to visualise stock performance of the company you selected:
a.	Candlestick graph v/s Volume: It is commonly used by financial analysts to understand the daily price trend against daily volume of transactions.
b.	Close Price graph: Simple raw time series the graph showing the variation of closing price.
c.	High v/s Low Graph: Showing the daily max and min of the stock price.
d.	Close v/s Low Graph: Showing the daily max and min price with closing price for the day.
e.	Linear Trendline: Best fit linear line for the closing price over the time.
f.	Normalised Closing Price v/s Volume: Comparing the closing price against volume by getting the y axis standardised to same range of 0-1.
g.	Simple Moving Average: It is commonly used in financial technical analysis to smooth the short-term fluctuations to understand the market trend; will require user to input a window size.
 
h.	Weighted Moving Average: It is used to understand market trend through focusing on the latest price by adding more weight to latest prices comparing to prior past data; will require user to input window size or weight.
i.	Bollinger Bands: Created to understand the price volatility over time and reflects if a stock oversold/overbought, will require to window size to smoothing the closing price using simple moving average.
j.	Moving average convergence/divergence: Displays the relationship between 12-period EMA and 26 period EMA to indicate the trend following momentum of the stock price
k.	Balance of power: Used by finance analyst to determine buying/selling trends and taking advantage of overbought/oversold situations.


Predictive Analysis:
On selecting descriptive analysis, you will be given two options as below:
1.	Predict stock price for the company using linear regression:
a.	Enter the from date and to date in format of (DD/MM/YYYY) for the duration you want to select as training window.
b.	Enter the prediction date (past/present/future) for which you want to see the predicted price according to linear regression model.
c.	The program will display the predicted price along with R2 error value and RMS Error value so that you can determine how accurately the price has been predicted. Also predicted price graph v/s actual price graph for the training window will be illustrated.
2.	Predict stock price by using ARIMA Model:
a.	Enter the from date and to date in format of (DD/MM/YYYY) for the duration you want to select as training window.
b.	Enter the prediction date (future) for which you want to see the forecast price according to linear regression model.
c.	The program will display the predicted price along with RMS Error value so that you can determine how accurately the price has been predicted. Also it will compare the actual price data used for testing the model within the training window v/s the predicted price for the tested price data.


Navigating tips:
Please follow up through the instructions of the program whenever you want to go back to previous screen or exit the program.
 
UML Diagram
The UML diagram can be seen in the 'read-me.pdf'





