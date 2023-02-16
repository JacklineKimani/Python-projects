# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:17:41 2023

@author: Mbutu
"""
from tabulate import tabulate

a = input("Give your name:")
b = input("Give your date of birth in the format Y/M/D:")
c = input("Give your email:")
d = input("Give your height:")
e = input("Give years of experience:")
f = input("Type 'Submit' to submit:")

if f == 'Submit':
    data = [['Name', 'Date of Birth', 'Email', 'Height', 'Experience'],[a,b,c,d,e]]
    print(tabulate(data))