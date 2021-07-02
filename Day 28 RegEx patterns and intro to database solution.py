# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:42:57 2021

@author: Yi
"""

import sys, re

names = []
pattern = re.compile('@gmail.com$')

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    if pattern.search(emailID):
        names.append(firstName)
names.sort()
for name in names:
    print(name)
    