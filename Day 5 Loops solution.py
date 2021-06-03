# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:18:30 2021

@author: Yi
"""

n = int(input("Enter an interger that is bigger than or equal to 2 and smaller than or equal to 20"))

for i in range(1, 11):
    results = n * i
    print(n, " x ", i, " = ", results)
    