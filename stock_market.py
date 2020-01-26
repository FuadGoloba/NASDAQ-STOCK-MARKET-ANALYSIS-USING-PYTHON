# -*- coding: utf-8 -*-
"""
#=============================================================================#
#Created on Fri Nov 15 13:28:26 2019                                          #
#                                                                             #
#author: Fuad Goloba/Darshan Amin/Alp Ates                                    #
#=============================================================================#
"""

#Packages
import company_detail as cd
import predictive_analysis as pa
import descriptive_analysis as da
from general_funtions import menu_head, clear_screen
from time import sleep
import warnings


#==============================================================================
#                Main funtion
#==============================================================================   

def main():
    
    #ignore all version related warnings being displayed
    warnings.filterwarnings('ignore')
    #get company list
    comp_list = cd.get_nasdaq_data()
    
    upd_flg = 0
    
    while upd_flg == 0:
        
        #clear screen and display output
        clear_screen()
        menu_head()
        #Initially display option to user to update nasdaq or proceed further
        print("Please select any either of the below options:- \n")
        print("Press 1 -> Update NASDAQ List\n")
        print("Press 2 -> Proceed further to select a company\n")
        print("Press any key to exit\n")
        
        first_input = input("Enter your option:- ")
        
        if first_input == "1":
            #Refresh Nasdaq 
            nasdaq_data = cd.refresh_nasdaq()
            #store the company list in a dictionary with ticker as key and company name as value  
            comp_list = nasdaq_data.to_dict()         
            print("\nNasdaq Database updated in system")
            sleep(1.0)
        elif first_input == "2":
            # Proceed further
            main_flag = 0
            while main_flag == 0:
                clear_screen()
                menu_head()
                #Input company ticker, Validate it and it corresponding company name
                company_ticker, company_name = cd.company_symbols(comp_list)
        
                #get company data till date
                comp_data = cd.get_company_data(company_ticker)
        
                flag_des_pres = 0
                while flag_des_pres == 0:
                    #Clear Screen and display header
                    clear_screen()
        
                    menu_head()
                    print("Company selected is {} -> {} \n".format(company_ticker, company_name)) 
            
                    #Display option to select presciptive or predictive or select new company
                    print("Please select any either of the below options:- \n")
                    print("Press 1 -> Descriptive Analysis\n")
                    print("Press 2 -> Predictive Analysis\n")
                    print("Press 3 -> Select new company\n")
                    print("Press any other key to quit\n")
        
                    des_pres_option = input("Enter your option:- ")
            
                    if des_pres_option == '1':
                        #Descriptive Analysis
                        da.descriptive(comp_data, company_ticker, company_name)
                    elif des_pres_option == '2':
                        #Prescriptive Analusis
                        pa.predictive(comp_data, company_ticker, company_name)
                    elif des_pres_option == '3':
                        #go back to main menu to select new company
                        flag_des_pres = 1
                    else:
                        #exit the program
                        flag_des_pres = 1
                        main_flag = 1
                        upd_flg = 1
        else:
            #Exit the program
            upd_flg = 1
                
            
        


    
#==============================================================================
#                Call Main Program
#==============================================================================   
            
#Call Main program
if __name__ == "__main__":
    
    main()
