# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:53:07 2021

@author: Yi
"""

n = int(input("Enter the number of pairs"))

t = []
for i in range(n):
    a = str(input("Enter the name of the contact"))
    b = int(input("Enter their phone number"))
    t.append((a, b))
print(t)
    
phoneBook = {}
phoneBook.update(t)
print(phoneBook)

for i in range(n):
    print(phoneBook.get(str(input("Enter the name you want to access"))))