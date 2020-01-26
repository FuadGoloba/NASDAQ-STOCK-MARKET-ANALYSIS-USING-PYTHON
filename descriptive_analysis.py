# -*- coding: utf-8 -*-
"""
#=============================================================================#
#Created on Fri Nov 15 13:28:26 2019                                          #
#                                                                             #
#author: Fuad Goloba/Darshan Amin/Alp Ates                                    #
#=============================================================================#
"""
#import packages
import numpy as np
import matplotlib.pyplot as plt
import general_funtions as gen 
from mpl_finance import candlestick_ohlc    
import matplotlib.dates as mpl_dates
   
#==============================================================================
#                 Descriptive Analysis Menu
#==============================================================================     
def descriptive(comp_data, cmp_tick, cmp_name):
    """Descriptive analysis menu"""
    
    des_flag = 0
    while des_flag == 0:
        
        #Clear Screen and display header 
        gen.clear_screen()
        gen.menu_head()
        
        #display option for descriptive
        print("Decriptive Analysis for {} -> {}\n".format(cmp_tick, cmp_name))
        print("Press 1 to see Statistics\n")
        print("Press 2 to see the Visualisation\n")
        print("Press 3 to go back\n")
        print("Press any other key to exit\n")
    
        desc_opt = input("Enter your option: ")
        
        if desc_opt == '1':
            statistics(cmp_tick, cmp_name, comp_data)
        elif desc_opt == "2":
            graphs(cmp_tick, cmp_name, comp_data)
        elif desc_opt == "3":
            des_flag = 1
        else:
            exit()
                 
#==============================================================================
#                 Descriptive statistics 
#==============================================================================                 
def statistics(cmp_tick, comp_name, stock_data):
    
    """Stock market descriptive stats"""
    
    #display menu header
    gen.clear_screen()
    gen.menu_head()
    print("Statistics for {} -> {}\n".format(cmp_tick, comp_name))

    #create a list of columns to be dispayed and pre define format
    format_tbl = "=" * 100
    format_col = "| {:<78} | {:>15} |"
    text_list = ["Percentage gain in Stock Price ", "Mean of closing share price  " , \
                 "Maximum closing share price " , "Minimum closing share price for " , 
                 "Range of closing Share price " , "25 % Quartile " ,\
                 "50 % Quartile for closing share price " , "75 % Quartile of closing share price ","Standard deviation of closing share price ",\
                 "Coefficient of Variance of closing share price "]

    #get from and to dates and filted company data
    frm_date, to_date, from_date_s, to_date_s, filter_data = gen.get_dates_data(stock_data, 0)
    
    #get the statistics related to data
    desc_data = filter_data["Close"].describe().round(2)

    #calculate and store statistics in dictionary 
    dict_close = {}
    try:
         dict_close["gain"] = round(((filter_data.Close[-1] - filter_data.Close[0])/filter_data.Close[0]) * 100, 2)
  
    except IndexError:
        dict_close["gain"] = float("nan")
        
    dict_close["mean"] = desc_data.loc["mean"]
    dict_close["maximum"] = desc_data.loc["max"]
    dict_close["minimum"] = desc_data.loc["min"]
    dict_close["range"] = round(dict_close["maximum"]- dict_close["minimum"], 2)
    dict_close["quart_25"] = desc_data.loc["25%"]
    dict_close["quart_50"] = desc_data.loc["50%"]
    dict_close["quart_75"] = desc_data.loc["75%"]
    dict_close["std"] = desc_data.loc["std"]
    dict_close["var"] = round(dict_close["std"]/dict_close["mean"], 2)
    
    #create a list of keys
    list_key = list(dict_close.keys())
    
    #display headers
    gen.clear_screen()
    gen.menu_head()
    print("\n Statistics for {} -> {} from {} to {}\n".format(cmp_tick, comp_name, from_date_s, to_date_s ))
    
    print(format_tbl)
    for i in range(len(text_list)):

            print(format_col.format(text_list[i], str(dict_close[list_key[i]])))
            
    print(format_tbl, "\n")
    
    #display options to go baack or quit
    print("Press 1 to go back\n")
    print("Press any key to exit\n")
    
    des_input = input("Enter your option: ")
    
    #quit program
    if des_input != "1":
        exit()
        
        
#==============================================================================
#                 Descriptive Graphs
#==============================================================================        

def graphs(cmp_tick, comp_name, stock_data):
    
    """Descriptive graphs """
    gen.clear_screen()
    gen.menu_head()
    print("\nVisualisation for {} -> {}\n".format(cmp_tick, comp_name))
    
        #get from and to dates and filted company data
    frm_date, to_date, from_date_s, to_date_s, filter_data = gen.get_dates_data(stock_data, 1)
 
    flag_graph = 0
    while flag_graph == 0:
        gen.clear_screen()
        gen.menu_head()
        print("\nList of Visualisation for {} -> {} from {} to {}\n".format(cmp_tick, comp_name, from_date_s, to_date_s ))
        print("Press 1 for Candlestick graph v/s Volume\n")
        print("Press 2 for Close Price\n")
        print("Press 3 for High v/s Low\n")
        print("Press 4 for Close v/s High v/s Low\n")
        print("Press 5 for Linear Trendline\n")
        print("Press 6 for Normalised Close Price v/s Volume\n")
        print("Press 7 for Simple Moving Average\n")
        print("Press 8 for Weighted Moving Average\n")
        print("Press 9 for Bollinger Band\n")
        print("Press 10 for Moving Average Convergence/Divergence\n")
        print("Press 11 for Balance of Power\n")
        print("Press 12 to go back to previous screen \n")
        print("Press any other key to exit\n")
        
        graph_opt = input("Select the option for the graph you want to see: ")
        
        if graph_opt == '1':
            #candle stick v/s volume
            candlestick(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
            
        elif graph_opt == '2':
            #closing price graph
            closing_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)

        elif graph_opt == "3":
            # high V/s low
            high_low_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)

        elif graph_opt == "4":
                # close vs high vs low
            close_highlow_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)

        elif graph_opt == "5":
            #linear trendline series
            linear_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
        
        elif graph_opt == "6":
            #Normalised closed price vs volume
            normalise_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
        
        elif graph_opt =="7":
            
            # Simple Moving Average
            sma_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
            
        elif graph_opt == "8":
            # Weighted moving average
            wma_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)

        elif graph_opt == "9":
            #bollinger band
            bollinger_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)             
                    
        elif graph_opt == "10":
            #MACD
            macd_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
            
        elif graph_opt == "11":
            # Display Balance of power
            bop_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s)
            
        elif graph_opt == "12":
            #Exit the graph screen
            flag_graph = 1
   
        else:
            #Quit program
            exit()
            

#==============================================================================
#                 Closing Price graph
#==============================================================================  
            
def closing_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """Closing price graph"""
    #close plot graph
    plt.figure(figsize=(15,6))
    plt.title("Closing Stock Prices for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s)) 
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.plot(filter_data.Close, label = "Closing price")
    plt.legend(loc = "best")
    plt.show()
    
#==============================================================================
#                 High vs low Price graph
#==============================================================================  

def high_low_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """High vs low graph"""
    # high V/s low graph
    plt.figure(figsize=(15,6))
    plt.title("High V/S Low Stock prices for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s))
    plt.plot(filter_data.High, "g", label = "High Price")
    plt.plot(filter_data.Low, "r", label = "Low Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()

#==============================================================================
#                 Close V/s High v/s Low graph
#==============================================================================      
def close_highlow_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """High vs low vs close graph """
    # close vs high vs low graph
    plt.figure(figsize=(15,6))
    plt.title("Close v/s High v/s Low of Stock prices for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s))
    plt.plot(filter_data.Close, "b", label = "Closing Price")
    plt.plot(filter_data.High, "g--", label = "High Price")
    plt.plot(filter_data.Low, "r--", label = "Low Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()
    
#==============================================================================
#                 Linear Trend Line graph
#==============================================================================      
def linear_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """Linar trend graph"""
    
    #divide x axis into n parts of data between 0 and 1
    date_x = np.linspace(0,1,len(filter_data.index))
    
    #create polynomial fit of degree 1
    poly_fit = np.polyfit(date_x, filter_data.Close, 1)
    #fit the 1 degree equation into 1D
    polyid = np.poly1d(poly_fit)
    #get the y axis trend
    trend =   polyid(date_x)
    
    #Plot linear trend line graph
    plt.figure(figsize=(15,6))
    plt.title("Linear trendline for {} -> {} from {} - {}".format(comp_name, cmp_tick, from_date_s, to_date_s))
    plt.scatter(filter_data.index, filter_data.Close, label = "Closing Price")
    plt.plot(filter_data.index ,trend, "r", label = "Linear trend for Closing Price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")
    plt.legend(loc = "best")
    plt.show()
    
 
#==============================================================================
#                 Simple Moving Averages graph
#==============================================================================  
    """Simple moving average"""
def sma_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    
    #get window size
    window_size = input ("Enter the window size: ")
    flag_w = False
    while flag_w == False:
        try:
            window_size = int(window_size)
            flag_w = True
        except ValueError:
            flag_w = False
            window_size = input ("Incorrect window size. Please enter the window size: ")
            
        #get y axis value of moving averages         
        moving_avg = filter_data.Close.rolling(window_size).mean() 
        
        #Plot moving averages
        plt.figure(figsize=(15,6))
        plt.title("Moving averages for {} -> {} from {} - {} for window size {}".format(cmp_tick, comp_name, from_date_s, to_date_s, str(window_size)))
        plt.fill_between(filter_data.index, filter_data.Close, label = "Closing Price")
        plt.plot(filter_data.index, moving_avg, "r", label = "SMA Window {}".format(str(window_size)))
        plt.xlabel("Time")
        plt.ylabel("Stock Price") 
        plt.legend(loc = "best")
        plt.show()    


#==============================================================================
#                 Weighted Moving Averages graph
#==============================================================================  
def wma_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    
    #get window size
            
    window_size = input ("Enter the window size: ")
    flag_win = False
    while flag_win == False:
        try:
            window_size = int(window_size)
            flag_win = True
        except ValueError:
            flag_win = False
            window_size = input ("Incorrect window size. Please enter the window size: ")
                    
    #get weight        
    flag_wht = False
    weight = input ("Enter the weight: ")
    while flag_wht == False:
        try:
            weight = int(weight)
            flag_wht = True
        except ValueError:
            flag_wht = False
            weight = input ("Incorrect weight. Please enter the correct weight: ")
    
    #create weight array                
    weight_array = np.linspace(weight ,1 , window_size)
    
    #Get sum of weights
    weight_sum = np.sum(weight_array)
    
    #get weighted moving average
    weight_move_avg = filter_data.Close.rolling(window_size).apply(lambda  price: np.sum(weight_array * price)/weight_sum, raw=True)
    
    #Plot weighted moving average
    plt.figure(figsize=(15,6))
    plt.title("Weighted moving average over 12 V/S 26 period for {} -> from {} - {} for window size {} and weight {}".format(cmp_tick, comp_name, from_date_s, to_date_s, window_size, weight))
    plt.fill_between(filter_data.index, filter_data.Close, label = "Closing Price")
    plt.plot(filter_data.index, weight_move_avg, "r", label = "WMA:- Weight {}, Window {}".format( str(weight), str(window_size)))
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()    
    
#==============================================================================
#                 Bollinger band graph
#==============================================================================    
def bollinger_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """Bollinger band graph"""
    #Get window size
    window_size = input ("Enter the window size: ")
    flag_w = False
    while flag_w == False:
        try:
            window_size = int(window_size)
            flag_w = True
        except ValueError:
            flag_w = False
            window_size = input ("Incorrect window size. Please enter the window size: ")
    
    #Get moving average       
    moving_avg = filter_data.Close.rolling(window_size).mean() 
    
    #get standard deviation
    std_dev = filter_data.Close.rolling(window_size).std() 
    
    #get upper band twice the std above moving avg
    upper_band = moving_avg + (std_dev * 2)
    
    #get lower band twice the std below moving avg
    lower_band = moving_avg - (std_dev * 2)
    
    #Plot bollinger band
    plt.figure(figsize=(15,6))
    plt.title("Bollinger Band  for {}  {}-> from {} - {} for window size {}".format(cmp_tick, comp_name, from_date_s, to_date_s, window_size))
    plt.plot(filter_data.index, moving_avg, "y", label = "MA - Window {}".format( str(window_size)))
    plt.fill_between(filter_data.index, upper_band, lower_band, color ="grey", label = "Bollinger Band")
    plt.plot(upper_band, "g", label = "Upper Bollinger band band")
    plt.plot(lower_band, "r", label = "Lower Bollinger band")
    plt.plot(filter_data.Close, "b", label = "Closing price")
    plt.xlabel("Time")
    plt.ylabel("Stock Price") 
    plt.legend(loc = "best")
    plt.show()
    
    
#==============================================================================
#                 Moving average convergence / divergence graph
#==============================================================================      
def macd_graph(comp_name ,filter_data, cmp_tick, from_date_s, to_date_s):
    """Moving average convergence/divergence gaph"""
    
    #get fast exponential moving average    
    f_ema = filter_data.Close.ewm(span = 12).mean()
    #get slow exponential moving average  
    s_ema = filter_data.Close.ewm(span = 26).mean()  
    
    #get macd
    macd = f_ema - s_ema
    
    #signal line has span 9
    signal_line = macd.ewm(span = 9).mean()
    
    #macd histogram
    #macd_his = np.array(macd - signal_line)
    
    #Plot MACD vs EMA        
    graph, plot = plt.subplots(2, sharex= True, figsize = (15,6))
    graph.suptitle("Moving average convergence/divergence against the Exponential Fast 12/Slow 26 Moving average for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s))  
    plot[0].set_title("Moving Average Convergence/Divergence")
    plot[0].plot(filter_data.index, macd, "r", label = "MACD")
    plot[0].plot(filter_data.index, signal_line, 'y', label = "Signal Line EMA 9")
    #plot[0].scatter(filter_data.index, macd_his, 'b', label = "MACD Histogram")
    plot[0].set_xlabel("Time")
    plot[0].set_ylabel("MACD") 
    plot[0].legend(loc = "best")
    plot[1].set_title("Exponential Moving Average")
    plot[1].plot(filter_data.index, f_ema, "g", label = "Fast EMA 12")
    plot[1].plot(filter_data.index, s_ema, "b", label = "Slow EMA 26")
    plot[1].set_xlabel("Time")
    plot[1].set_ylabel("Stock Price") 
    plot[1].legend(loc = "best")
    graph.show()
    
#==============================================================================
#                 Balance of power graph
#==============================================================================      
def bop_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    """Balance of power grap"""
    bop = ((filter_data.Close - filter_data.Open)/(filter_data.High - filter_data.Low))
                        
    # smothening BOP by applying moving average to it 
    window_size = input ("Enter the window size: ")           
    flag_w = False
    while flag_w == False:
        try:
            window_size = int(window_size)
            flag_w = True
        except ValueError:
            flag_w = False
            window_size = input ("Incorrect window size. Please enter the window size: ")
            
    #smothing BOP by MA
    bop_ma = bop.rolling(window_size).mean() 

    #Plot balace of power v/s closing price
    graph, plot = plt.subplots(2, sharex= True, figsize = (15,6))
    graph.suptitle("Balance of Power compared with Closing price {} -> {} from {} - {} for window size {}".format(cmp_tick, comp_name, from_date_s, to_date_s, str(window_size)))  
    plot[0].set_title("Balance of Power")
    plot[0].plot(filter_data.index, bop_ma, "r", label = "Balance of Power")
    plot[0].set_xlabel("Time")
    plot[0].set_ylabel("BOP") 
    plot[0].legend(loc = "best")
    plot[1].set_title("Closing price")
    plot[1].plot(filter_data.index, filter_data.Close, "g", label = "Closing Price")
    plot[1].set_xlabel("Time")
    plot[1].set_ylabel("Stock Price") 
    plot[1].legend(loc = "best")
    graph.show()  
    
#==============================================================================
#                 Normalised stock price
#============================================================================== 

def normalise_graph(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    
    """normalised price graph"""
    
    #get closing price stats
    close_describe = filter_data.Close.describe()
    
    #max closing price
    max_close = close_describe.loc["max"]
    
    #min closing price
    min_close = close_describe.loc["min"]
    
    #calcuate the denominator of closing price normalization
    denom_close = max_close - min_close
    
    #get closing price in numpy array
    close = np.array(filter_data.Close)
    
    #get volume stats
    vol_describe = filter_data.Volume.describe()
    
    #get Max volume
    max_vol = vol_describe.loc["max"]
    
    #get min volume
    min_vol = vol_describe.loc["min"]
    
    #calcuate the denominator of volume normalization
    denom_vol = max_vol - min_vol
    
    #get volume in numpy array
    volume = np.array(filter_data.Volume)
    

    #Normalise the closing price
    for i in range(len(close)):
        close[i] = (close[i] - min_close)/denom_close
        volume[i] = (volume[i] - min_vol)/denom_vol
    
    #Plot graph
    plt.figure(figsize=(15,6))
    plt.title("Normalised Closing Stock Prices v/s Volume for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s))
    plt.plot(filter_data.index, close, 'r', label = "Normalised Closing Price")
    plt.bar(filter_data.index, volume, label = "Normalised Volume")
    plt.xlabel("Time")
    plt.ylabel("Normalised Value") 
    plt.legend(loc = "best")
    plt.show()
    
#==============================================================================
#                 Candle stick
#==============================================================================     
    

def candlestick(comp_name, filter_data, cmp_tick, from_date_s, to_date_s):
    
    #sort data into open, high, low, close format
    filter_prices = filter_data.loc[: , ["Open", "High", "Low", "Close"]]
    
    #Reset index to get dates as a seperate column
    filter_prices = filter_prices.reset_index()
    
    #conver date to numbers
    filter_prices['Date'] = filter_prices['Date'].apply(mpl_dates.date2num)
    
    #convert to float
    filter_prices = filter_prices.astype(float)
    
    #Create subplot
    graph, plot = plt.subplots( 2 ,sharex= True, figsize = (15,6))
    
    #create candle stick graph on plot
    candlestick_ohlc(plot[0], filter_prices.values, width = 0.3, colorup = "green", colordown = "red")
    
    #convert number back to dates
    dates_from_num = mpl_dates.DateFormatter('%d-%m-%Y')
    graph.suptitle("Candlestick graph v/s Volume for {} -> {} from {} - {}".format(cmp_tick, comp_name, from_date_s, to_date_s))
    plot[0].set_title("Candlestick Graph")
    plot[0].xaxis.set_major_formatter(dates_from_num)
    plot[0].set_ylabel("Stock Price")
    plot[1].set_title("Volume")
    plot[1].bar(filter_data.index, filter_data.Volume)
    plot[1].set_xlabel("Time")
    plot[1].set_ylabel("Volume")
    plt.show()
    
