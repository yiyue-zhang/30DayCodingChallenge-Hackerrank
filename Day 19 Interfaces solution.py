# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:12:03 2021

@author: Yi
"""
#I did not write those codes

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        temp = []
        for i in range(1, n+1):
            if n%i == 0:
                temp.append(i)
        return sum(temp)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)