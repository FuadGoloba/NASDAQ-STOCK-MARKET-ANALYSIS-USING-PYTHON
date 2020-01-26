# -*- coding: utf-8 -*-
"""
#=============================================================================#
#Created on Fri Nov 15 13:28:26 2019                                          #
#                                                                             #
#author: Fuad Goloba/Darshan Amin/Alp Ates                                    #
#=============================================================================#
"""

#Import functions
import datetime as dt
from os import system, name 

#==============================================================================
#                 Menu header
#============================================================================== 
def menu_head():
    """Main menu for header"""
    print("*" * 100)
    print("|{:=^98}|".format("NASDAQ STOCK MARKET"))
    print("*" * 100)
    print("\n")
    
#==============================================================================
#                 Funtion to validate input date
#============================================================================== 
def input_date_validate(text, switch):
    """" Validate input date"""
    
    #get date from user
    if switch == 0:
        date_str = input(f"Enter {text} (DD/MM/YYYY): ")
    elif switch == 1:
        date_str = input(f"To date is earlier than from date. Please enter correct to date again (DD/MM/YYYY): ")
    elif switch == 2:  
        date_str = input(f" Prediction date is earlier than to date of window. Please enter correct prediction again (DD/MM/YYYY): ")
    elif switch == 3:  
        date_str = input(f" To date is earlier than or equal to from date. Please enter correct prediction again (DD/MM/YYYY): ")    
     
    #check if date entered is valid    
    dateformat = False
    
    while dateformat == False:
        #check date is split properly
         
        try:
            day, month, year = date_str.split("/")
            try:
                correct_date = dt.date(int(year),int(month), int(day))
                dateformat = True
            except ValueError:
                date_str = input(f"Invalid date entered. Please enter {text} again (DD/MM/YYYY): ")
        except ValueError:
            date_str = input(f"Invalid date entered. Please enter {text} again (DD/MM/YYYY): ") 
            
                     
    return correct_date   
            
                
#==============================================================================
#                 get from and to dates and filter data
#==============================================================================   

def get_dates_data(stock_data, switch):
    
        #input from date and validate it
    frm_date = input_date_validate("from date", 0) 
    
    #input to date and validate it 
    to_date = input_date_validate("to date", 0)  
    
    #check if to date less than from date
    if switch == 0:
        #for statistics frm and to date can be equal
        while to_date < frm_date:
            to_date = input_date_validate("to_date", 1)
    elif switch == 1:
        #for graph from and to date cannot be equal
        while to_date <= frm_date:
            to_date = input_date_validate("to_date", 3)
        

    #get date in string format
    from_date_s = str(frm_date.strftime("%d/%m/%Y"))
    to_date_s = str(to_date.strftime("%d/%m/%Y"))
    
        #if frm date less than lowest date available then from date
    #for processing is lowest date available
    if ( frm_date < stock_data.index[0].date()):
        frm_date = stock_data.index[0].date()
      
    #if to date greater than highest date available then from date
    #for processing is highest date available        
    if (to_date > stock_data.index[-1].date()):
        to_date = stock_data.index[-1].date()
        
        #filter the data we need from the entire company data we have    
    filter_data = stock_data.loc[frm_date:to_date]    
    
    return frm_date, to_date, from_date_s, to_date_s, filter_data

#==============================================================================
#                 clear screen
#==============================================================================   

def clear_screen():
    """Function to clear screen"""
    #if windows
    if name == 'nt':
        system('cls')
        #any other systems other than windowss
    else:
        system('clear')


                
                
                
                
        
            
 
            
 
