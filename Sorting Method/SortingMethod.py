# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:25:39 2023

@author: Mbutu
"""

sort = input("Type A to sort aLphabetically or Type N to sort numerically:")
b = input("Type C if the words are separated with a comma or S if separated with a space:")
a = input("Input words to be sorted:")

if sort == 'A':
    if b == 'C':  
        mylist = a.split(",")
    else:
        if b == 'S': 
            mylist = a.split()
    choose = input("Type A for ascending order or Type D for descending order:")    
    if choose == "A":
        mylist.sort(key=str.lower)
        print(mylist)
    else:
        if choose=="D":
            mylist.sort(key=str.lower,reverse= True)
            print(mylist)
else:
    if sort == 'N':
       if b == 'C':  
           x = a.split(",")
       else:
           if b == 'S': 
               x = a.split()
    choose = input("Type A for ascending order or Type D for descending order:")    
    if choose == "A":
        mylist= list(map(int, x))
        mylist.sort()
        print(mylist)
    else:
        if choose=="D":
           mylist= list(map(int, x))
           mylist.sort(reverse= True)
           print(mylist)