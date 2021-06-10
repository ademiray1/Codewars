# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def pattern(n):
    # Happy Coding ^_^
    
    
    result = ''
    for i in range(1, n + 1):
        result += str(i) * i + '\n'
    return result[:]

print(pattern(5))

#%%
def pattern(n):
    
    return '\n'.join(str(i) * i for i in range(1, n + 1))

print(pattern(5))
