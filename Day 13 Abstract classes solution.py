# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:03:42 2021

@author: Yi
"""

from abc import ABCMeta

class book(object):
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    def display(self): 
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)

a = book("The Alchemist", "Paulo Coelho", 248)
a.display()