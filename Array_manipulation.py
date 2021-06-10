# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s

"""
"""
Given an array of positive integers, replace every element with the least greater element to its right. If there is no greater element to its right, replace it with -1. For instance, given the array

[8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28],

the desired output is

[18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1].

Your task is to create a function "arrayManip()" that takes in an array as its argument, manipulates the array as described above, then return the resulting array.

Note: Return a new array, rather than modifying the passed array.

"""
#Array Manipulation

    
def array_manip(array):
    
    final_list = []
    
    for i in range(len(array)):
        new_list = []

        for a in array[i+1:]:
         #   print(a)
            if array[i] < a:
                new_list.append(a)
            print(new_list)   
        my_val = min(new_list,default = -1)
        final_list.append(my_val)
    return final_list
                
#%%
def array_manip(array):

    final_list = []

    for i in range(len(array)):
        
        min_list = []
        
        for a in array[i+1:]:
            
            if a > array[i]:
                min_list.append(a)
        min_val = min(min_list, default = -1)
        
        final_list.append(min_val)
    
    return final_list
        
        
    
array = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]

print(array_manip(array))


#%%
def array_manip(array):
    return [min([a for a in array[i+1:] if a > array[i]], default=-1) for i in range(len(array))]

#%%

def array_manip(array):
    return [min((r for r in array[i:] if r > n), default=-1) for i, n in enumerate(array, 1)]


#%%
    
def min_max(lst):
    
    return list((min(lst),max(lst)))


lst = [1,5]

print(min_max(lst))