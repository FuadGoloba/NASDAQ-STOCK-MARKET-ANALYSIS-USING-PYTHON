# -*- coding: utf-8 -*-
"""
#=============================================================================#
#Created on Fri Nov 15 13:28:26 2019                                          #
#                                                                             #
#author: Fuad Goloba/Darshan Amin/Alp Ates                                    #
#=============================================================================#
"""
#import Packages
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import general_funtions as gen
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pmdarima.arima import auto_arima


#==============================================================================
#                 Descriptive Analysis Menu
#==============================================================================     
def predictive(comp_data, cmp_tick, cmp_name):
    """Descriptive analysis menu"""
    
    des_flag = 0
    while des_flag == 0:
        
        #Clear Screen and display header
        gen.clear_screen()
        gen.menu_head()
        
        #display option for descriptive
        print("Predictive Analysis for {} -> {}".format(cmp_tick, cmp_name))
        print("\n")
        print("Press 1 to see stock prediction using Linear Regression\n")
        print("Press 2 to see stock prediction using ARIMA\n")
        print("Press 3 to go back\n")
        print("Press any other key to exit\n")
    
        desc_opt = input("Enter your option: ")
        
        if desc_opt == '1':
            linear_regression(comp_data, cmp_tick, cmp_name)
        elif desc_opt == "2":
            arima_prediction(comp_data, cmp_tick, cmp_name)
        elif desc_opt == "3":
            des_flag = 1
        else:
            exit()


#==============================================================================
#                 Linear regression
#==============================================================================                
def linear_regression(cmp_data, cmp_tick, cmp_name):
    
    """Perform Linear regression prediction"""
    
    #Clear the screen and display main header
    gen.clear_screen()
    gen.menu_head()
    
    print("Stock Price Prediction for {} -> {} using Linear Regression".format(cmp_tick, cmp_name))
    
         #if there was a holiday or weekend then fill the data of the holiday/weekend
     #with the data for previous working day as the price wont change during holiday
     #and the next working day will open with the closing price of last woking day
    cmp_data = cmp_data.resample("D").ffill()
    
    #get from and to dates and filted company data
    frm_date, to_date, from_date_s, to_date_s, filter_data = gen.get_dates_data(cmp_data, 1)
    
         
     #get prediction date from user    
    predict_date = gen.input_date_validate("prediction date", 0) 
    
    predict_dt_s = str(predict_date.strftime("%d/%m/%Y"))
     
    #get the range of dates within training window
    filter_date = np.array(filter_data.index) 
    
    #get closing price in an n x 1 array
    filter_close = np.array(filter_data.Close).reshape(len(filter_data.Close), 1)
    
    #convert dates into index starting from 0 and store it in n x 1 array
    filter_days = np.arange(0, len(filter_date)).reshape(len(filter_date), 1)
     
    #divide the training window into 80% test and 20% training window
    xdays_train, xdays_test, yclose_train, yclose_test = train_test_split(filter_days, filter_close, test_size = 0.2)
    
    #initiate linear regression
    linear_reg = LinearRegression()
    
    #Train the regression training window
    linear_reg.fit(xdays_train, yclose_train)
     
    #test the regression model and get the r^2 value (self confidence)
    linear_self_conf = linear_reg.score(xdays_test, yclose_test)
    print("R Square Value is:", round(linear_self_conf, 2))
     
    #get the root mean square error value
    rt_mean_err = sqrt(np.mean((linear_reg.predict(xdays_test) - yclose_test)**2))
    print("Root mean square error is: ", round(rt_mean_err, 2))
    
    #predict the prices in the training window
    close_predict = linear_reg.predict(filter_days)

    #calculate no of days between prediction date and from date of training window
    days_dif = np.array((predict_date - frm_date).days).reshape(-1,1)
    
    #get the predicted price for predicted date
    predict_lr = linear_reg.predict(days_dif)
    print("Predicted price for {} on {} is: {}".format(cmp_tick, predict_dt_s, str(round(predict_lr[0][0], 2))))
    
    #Plot predicted v/s actual closing price for the training period
    plt.figure(figsize=(15,6))
    plt.title("Actual V/S Predicted Closing Price  for {} -> {} from - {} Training Window".format(cmp_tick, cmp_name, from_date_s, to_date_s))
    plt.plot(filter_data.index, filter_data.Close, "g", label = "Actual Closing Price")
    plt.plot(filter_data.index, close_predict, "r", label = "Predicted Closing Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()
    
    #display options to go baack or quit
    print("\n")
    print("Press 1 to go back\n")
    print("Press any key to exit\n")
    
    lr_input = input("Enter your option: ")
    
    if lr_input != "1":
        exit()

#==============================================================================
#                 Arima Prediction
#==============================================================================   
def arima_prediction(cmp_data, cmp_tick, cmp_name):
    """Arima Model Prediction using Auto arima"""
    #Clear the screen and display main header
    gen.clear_screen()
    gen.menu_head()
    
    
    print("Stock Price Prediction for {} -> using ARIMA\n".format(cmp_tick, cmp_name))
    
         #if there was a holiday or weekend then fill the data of the holiday/weekend
     #with the data for previous working day as the price wont change during holiday
     #and the next working day will open with the closing price of last woking day
    cmp_data = cmp_data.resample("D").ffill()
    
        #get from and to dates and filted company data
    frm_date, to_date, from_date_s, to_date_s, filter_data = gen.get_dates_data(cmp_data, 1)
         
     #get prediction date from user    
    predict_date = gen.input_date_validate("prediction date", 0) 
    
    while predict_date <= to_date:
        predict_date = gen.input_date_validate("prediction date", 2) 

    
    predict_dt_s = str(predict_date.strftime("%d/%m/%Y"))
   
    #get clsing price for the window
    closing_price = filter_data.Close
    
    #set initial 80 % as training and last 20 % as testing
    closing_training = closing_price[:int(0.8*(len(closing_price)))]
    closing_test = closing_price[int(0.8*(len(closing_price))):]
    
    #Train Arima using Auto arima function
    closing_arima = auto_arima(closing_training, error_action = 'ignore', suppress_warnings = True) 
    closing_arima.fit(closing_training)
    
    #Predict the Test period closing price
    close_test_pred = closing_arima.predict(n_periods = len(closing_test))
    
    #get RMSE Value
    close_rmse = sqrt(mean_squared_error(closing_test, close_test_pred))
    print("Root mean square error is: {}".format(str(round(close_rmse, 2))))
    
    #calculate no of days between prediction date and to date of training window
    days_dif = int((predict_date - to_date).days)
    
    #predict Price of prediction date
    close_predict = closing_arima.predict(n_periods = days_dif)
    print("Predicted price for {} on {} is: {}".format(cmp_tick, predict_dt_s, str(round(close_predict[-1], 2))))
    
    #plot actual vs predicted
    plt.figure(figsize=(15,6))
    plt.title("Actual V/S Predicted Closing Price  for {} -> {} from {} - {} Training Window".format(cmp_tick, cmp_name, from_date_s, to_date_s))
    plt.plot(closing_training, "g", label = "Actual Closing Price")
    plt.plot(closing_test, "y", label = "Actual Closing period used for test")
    plt.plot(closing_test.index, close_test_pred, "r", label = "Predicted Test Closing price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()
    
    #display options to go baack or quit
    print("\nPress 1 to go back\n")
    print("Press any key to exit\n")
    
    ar_input = input("Enter your option: ")
    
    if ar_input != "1":
        exit()
    
        
