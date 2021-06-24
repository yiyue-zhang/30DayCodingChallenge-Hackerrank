# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:37:37 2021

@author: Yi
"""

#I did not write this solution because I did not understand the prompt

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        n = Node(data)
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = n
            return head
        else:
            return n

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  