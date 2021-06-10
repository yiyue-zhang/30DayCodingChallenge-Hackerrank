# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:14:30 2021

@author: Yi
"""


def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x - 1))

N = int(input("Enter an integer"))
print(factorial(N))