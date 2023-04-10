# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:41:00 2023

@author: Mbutu
"""

import string
import pandas as pd

#Generate alphabet
x = list(string.ascii_lowercase)
#Generate numbers for the alphabet1
y = [i for i in range(1,27)]

#Function for encoding
def encode(w): 
    z = pd.Series(y, index= x)
    try:
        for i in w:
            s = z[i]
            print(s)
    except KeyError:
        print("Use the right format.")
        
#Function for decoding  
def decode(bb):
    z = pd.Series(x, index= y)
    try:
        for i in bb:
            a = int(i)
            s = z[a]
            print(s)
    except KeyError:
        print("VALUE OUT OF RANGE!!\nType numbers in the range 1-26!!")
    except ValueError:
        print("Use the right format.")

#Word input and decode/encoder choice      
choice = input("Type E for encode or D for decode:")


if choice == 'E':
        word = input("Give input(lowercase):")
        encode(word)
elif choice == 'D':
        word = input("Give input(split by space):")
        q = word.split()
        decode(q)
    
