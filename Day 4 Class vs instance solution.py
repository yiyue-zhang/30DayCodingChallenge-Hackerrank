# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:40:32 2021

@author: Yi
"""

class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0 
        else:
            self.age = initialAge
            
    def amIOld(self):
        if self.age < 13:
            return("You are young.")
        elif (self.age >= 13) & (self.age < 18):
            return("You are a teenager.")
        else:
            return("You are old.")
            
    def yearPasses(self):
        self.age += 1 
        if self.age < 13:
            return("You are young.")
        elif (self.age >= 13) & (self.age < 18):
            return("You are a teenager.")
        else:
            return("You are old.")

i = Person(17)
print(Person.amIOld(i))
print(Person.yearPasses(i))