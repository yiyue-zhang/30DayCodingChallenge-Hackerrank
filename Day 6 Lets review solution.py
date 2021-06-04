# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:57:20 2021

@author: Yi
"""

t = int(input("Please enter the number of test case"))

l = []
for i in range(t):
    l.append(str(input("Please enter a string that is less than 10000 letters but more than 2 letters")))

for i in range(t):
    s = l[i]
    print(s[::2], s[1::2])