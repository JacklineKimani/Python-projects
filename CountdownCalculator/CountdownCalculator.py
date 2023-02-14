# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:23:16 2023

@author: Mbutu
"""

from datetime import datetime
from dateutil import relativedelta
from tabulate import tabulate
from datetime import timedelta

conv = input("Type: \nH:M:S for Hours, Minutes and Seconds or \nY/M/D for Years,  Months and Days or \nAD to add days to a date or \nSD to subtract days from a date: ")

if conv == 'Y/M/D':
    str_d1= input("Input the earlier date in the format, Y/M/D:")
    str_d2= input("Input the later date in the format, Y/M/D:")
    
    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y/%m/%d")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d")
    
    # difference between dates in timedelta
    delta = relativedelta.relativedelta(d2, d1)
    print('Years, months, days between the two dates is:')
    data = [['Years', 'Months', 'Days'], [abs(delta.years),abs(delta.months), abs(delta.days)]]
    print (tabulate(data))
    delta2 = d2-d1
    d = delta2.days
    d3 = d*24
    d4 = d3*60
    d5 = d4*60
    data = [['T-Days','T-Hours', 'T-Minutes', 'T-Seconds'], [abs(d), abs(d3), abs(d4), abs(d5)]]
    print("The total time is:")
    print (tabulate(data))
else:   
    if conv == 'H:M:S':
        str_d1= input("Input the earlier time in the format, H:M:S:")
        str_d2= input("Input the later time in the format, H:M:S:")
        
        # convert string to date object
        d1 = datetime.strptime(str_d1, "%H:%M:%S")
        d2 = datetime.strptime(str_d2, "%H:%M:%S")
        
        # difference between dates in timedelta
        delta = relativedelta.relativedelta(d2, d1)
        data = [['Hours', 'Minutes', 'Seconds'], [abs(delta.hours), abs(delta.minutes), abs(delta.seconds)]]
        print("The total time in Hours, Minutes and seconds is:")
        print (tabulate(data))
        delta2 = d2-d1
        d = round(delta2.total_seconds(), 2)
        d3 = round(d/60, 2)
        d4 = round(d3/60, 2)
        data = [['Total Hours', 'Total Minutes', 'Total Seconds'], [abs(d4), abs(d3),abs(d)]]
        print("The total time is:")
        print (tabulate(data))
    else:
        if conv == 'AD':
            str_d1= input("Initial day in format Y/M/D:")
            str_d2= input("Number of days to add in number format:")
            d1 = datetime.strptime(str_d1, "%Y/%m/%d")
            d2 = int(str_d2)
            
            d3 = d1+timedelta(days= d2)
    
            print ("\nThe date is:", d3)
        else:
            if conv == 'SD':
                str_d1= input("Initial day in format Y/M/D:")
                str_d2= input("Number of days to subtract in number format:")
                d1 = datetime.strptime(str_d1, "%Y/%m/%d")
                d2 = int(str_d2)
                
                d3 = d1-timedelta(days= d2)
                
                print ("\nThe date is:", d3)  
            else:
                print("ERROR!!")