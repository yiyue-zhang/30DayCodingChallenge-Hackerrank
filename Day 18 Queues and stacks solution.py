# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:05:53 2021

@author: Yi
"""

class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []
    def pushCharacter(self,obj):
        self.stack.append(obj)
    def enqueueCharacter(self,obj):
        self.queue.append(obj)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop(0)