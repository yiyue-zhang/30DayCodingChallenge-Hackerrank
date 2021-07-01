# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:35:25 2021

@author: Yi
"""

# I did not write those codes because I did not understand binary

def getHeight(self,root):
    leftH = self.getHeight(root.left) if root.left else -1
    rightH = self.getHeight(root.right) if root.right else -1
    return leftH+1 if leftH > rightH else rightH+1