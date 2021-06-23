# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:25:02 2021

@author: Yi
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.maximumDifference = 0
        for x in range(len(a)):
            for y in range(x,len(a)):
                if abs(a[x] - a[y]) > self.maximumDifference:
                    self.maximumDifference = abs(a[x] - a[y])