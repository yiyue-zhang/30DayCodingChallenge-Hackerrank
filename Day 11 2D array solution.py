# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:02:35 2021

@author: Yi
"""

#Again, I did not write those codes because I could not figure it out

import math
import os
import random
import re
import sys

arr = []

for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
   
maxi = 0

for i in range(4):
    for j in range(4):
        current = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if maxi == 0 or current > maxi:
            maxi = current
print(maxi)
