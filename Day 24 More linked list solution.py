# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def removeDuplicates(self,head):
    node = head
    while node:
          if node.next:
             if node.data == node.next.data:
                node.next = node.next.next
             else:
                node = node.next
          else:
            node = node.next
    return head