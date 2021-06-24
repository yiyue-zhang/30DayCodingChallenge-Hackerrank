# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:40:03 2021

@author: Yi
"""

s = input("Please enter an integer")

try:
    print(int(s))
except ValueError:
    print("Bad String")