# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:38:50 2021

@author: Yi
"""

N = int(input("Enter the number of integers in an array"))
S = input("Enter all integers in the array")

A = []
for i in range(1, N + 1):
     A.append(S[-i])
print(*A, sep = '')