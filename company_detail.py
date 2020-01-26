# -*- coding: utf-8 -*-
"""
#=============================================================================#
#Created on Fri Nov 15 13:28:26 2019                                          #
#                                                                             #
#author:  Fuad Goloba/Darshan Amin/Alp Ates                                   #
#=============================================================================#
"""
#import Function
import pandas as pd
import pandas_datareader as pdr
import datetime as dt


#==============================================================================
#                Get list of companies
#==============================================================================     

def get_nasdaq_data():
        #check if NASDAQ company details are present in computer
    flag = 0
    try:
        #nasdaq_data = pd.read_csv("nasdaq.csv" ,index = "Symbol" , delimiter =",")
        nasdaq_data = pd.read_csv("nasdaq.csv" , index_col = 0, delimiter =",")
    except FileNotFoundError:
        flag = 1
    
    #if nasdaq data not present on computer then get list of companies from NASDAQ Website API
    if flag == 1:       
        #GET NASDAQ data
        nasdaq_data = refresh_nasdaq()
        
    #store the company list in a dictionary with ticker as key and company name as value   
    company_detail = nasdaq_data.to_dict()
    return company_detail  

#==============================================================================
#                 Refresh Nasdaq data
#============================================================================== 

def refresh_nasdaq():
    try:
        nasdaq_data = pd.read_csv("https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download", index_col = 0, delimiter =",")
    except:
        raise("Failed to get ticker data from NASDAQ")
        
    #Remove unncessary columns from data frame to keep only symbol as index and company name
    #nasdaq_data = nasdaq_data.drop(["Nasdaq Traded", "Listing Exchange","Market Category","ETF","Round Lot Size","Test Issue","Financial Status","CQS Symbol","NextShares", "NASDAQ Symbol"], axis = 1)   
    nasdaq_data = nasdaq_data.drop(nasdaq_data.columns[1:], axis = 1)
     #Store the Nasdaq company list on Computer in CSV File
    nasdaq_data.to_csv("nasdaq.csv", index = True)  
    
    return nasdaq_data
    
#==============================================================================
#                 Function to Create Company list file and load data
#============================================================================== 
    
def company_symbols(comp_list):
    """Check if list of all companies are already in computer if not then get the date via API
       and store it in computer. When the user passes Ticker as input it will be validated using the file."""
    
    # Get company ticker as input from user
    company_tick = input("Enter Company Symbol:- ")
    company_tick = company_tick.upper()  
    
    #Check if company ticker is string and present in list of companies of NASDAQ
    flag = 0
    while flag == 0:
        if type(company_tick) == str and company_tick in comp_list["Name"].keys():
            flag = 1
        else:
            flag = 0
            company_tick = input("Invalid company symbol. Please enter Company Symbol:- ")
            company_tick = company_tick.upper()  
            
    #Pass company ticker and name as output of function       
       
    company_name = comp_list["Name"][company_tick]       
    return company_tick, company_name

#==============================================================================
#                 Function to  Company symbol file and load data
#============================================================================== 

def get_company_data(cmp_ticker):
    """Get company data till date"""
    
    flag = 0
    #Create file name
    company_file = cmp_ticker + ".csv"
    first_data_date = dt.date(1970,1,1) #date from which data is available in web service
    todays_date = dt.date.today()
 
    #get company details from computer
    try:
        company_data = pd.read_csv(company_file, index_col = 0, delimiter = ",")
    except FileNotFoundError:
        flag = 1
    
    #if company details not found on coputer then get company detail from server
    if flag == 1:
        try:
            company_data = pdr.get_data_yahoo(cmp_ticker, first_data_date, todays_date)
        except: 
            raise("Server Error.....Unable to get data")
        
        company_data.to_csv(company_file, index = True) 
    
    #convert index date from string to date time format    
    company_data.index = pd.to_datetime(company_data.index)
    
        #Get the last date 

    last_date = company_data.index[-1].date()

    #if program executed tomorrow then get only tomorrows data and put it in csv file and dataframe
    if last_date < todays_date:
        next_date = last_date + dt.timedelta(days = 1)
        try:
            #get the remaining data till today and append to csv
            append_comp_data = pdr.get_data_yahoo(cmp_ticker, next_date, todays_date)
            company_data = company_data.append(append_comp_data)
            company_data.to_csv(company_file, index = True) 
        except:
            print("\nServer Error.....Unable to get data\n")
    
    #keeping unique date index
    company_data = company_data[~company_data.index.duplicated(keep='first')]
    return company_data
