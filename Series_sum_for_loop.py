# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def series_sum(n):
    # Happy Coding ^_^
    sums = 0
    
    k = 1
    
    for i in range(1,n+1):
        
        print(i)
        
        sums += float(1/k)
        
        k+=3
        
        
    
    return ("%.2f" % sums)
 
        
print(series_sum(3))