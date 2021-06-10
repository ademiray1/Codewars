# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""
#Codewars Grosshopper_summation

def summation(num):
    pass # Code here

    sum = 0
    for i in range(num+1):
 #       print(i)
        
        sum +=i
    
    return sum
    
print(summation(1))


#%%Best practices

def summation(num):
    return sum(xrange(num + 1))

#%%
    
def summation(num):
    return sum(range(1,num+1))
