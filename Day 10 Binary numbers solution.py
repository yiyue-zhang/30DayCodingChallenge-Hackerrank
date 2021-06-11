# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:17:34 2021

@author: Yi
"""

#Disclaimer: I did not write those codes because I do not understand binaries...

import sys, math

n = int(input("Please enter an integer"))
c = 0
m = 0

while n > 0:
    if n % 2 == 1:
        c += 1
    else:
        if c > m:
            m = c
        c = 0
    n = math.floor(n / 2)
if c > m:
    m = c
    
print(m)