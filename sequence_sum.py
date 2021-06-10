# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""

#Sum of Sequence

def sequence_sum(begin_number, end_number, step):
    #your code here
    
    seq_sum = 0
    
    for i in range(begin_number, end_number+1,step):
         print(i)   
         seq_sum +=i    
        
    return seq_sum


print(sequence_sum(2, 6,2))        


#%%Best practice
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))