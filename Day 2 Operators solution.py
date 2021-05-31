# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:17:18 2021

@author: Yi
"""

mealCost = float(input('Enter the cost of the meal before tax and tip'))
tipPercent = int(input('Enter the percentage of the cost of the meal being added as tip'))
taxPercent = int(input('Enter the percentage of the tax of the meal being added as tax'))
x = round(mealCost + mealCost * tipPercent / 100 + mealCost * taxPercent / 100)
print('The total cost of a meal is ', x)
