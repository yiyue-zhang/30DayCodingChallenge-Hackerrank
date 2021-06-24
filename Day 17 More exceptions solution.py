# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:44:10 2021

@author: Yi
"""

class myCalculator:
    def power(self,n,p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        elif p == 0:
            return 1
        else:
            pp = pow(n, p)
            return pp

T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   