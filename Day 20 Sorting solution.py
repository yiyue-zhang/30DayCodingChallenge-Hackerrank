# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:14:31 2021

@author: Yi
"""
#I did not write those codes

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nofswap = 0
for i in range(0,n-1):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            nofswap +=1

print("Array is sorted in", nofswap, "swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])