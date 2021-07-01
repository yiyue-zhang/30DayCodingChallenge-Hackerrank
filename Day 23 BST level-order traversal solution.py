# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:38:08 2021

@author: Yi
"""
# I did not write those codes because I did not understand binary

def levelOrder(self,root):
    leafs = [root]
    while len(leafs) > 0:
        leaf = leafs.pop(0)
        print(leaf.data, end=" ")
        if leaf.left:
            leafs.append(leaf.left)
        if leaf.right:
            leafs.append(leaf.right)