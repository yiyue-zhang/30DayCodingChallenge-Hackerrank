# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:06:35 2021

@author: Yi
"""

n = int(input('Enter an interger that is bigger than or equal to 1 but smaller than or equal to 100'))

if n % 2 != 0:
    print("Weird")
elif n in range(2,6):
    print("Not weird")
elif n in range(6,21):
    print("Weird")
else:
    print("Not weird")