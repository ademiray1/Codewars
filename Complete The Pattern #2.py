# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def pattern(n):
    # Happy Coding ^_^
    
    a= ''
        

    for i in range(0, n):
        
       # print(i)
        
        list_number = list(range(n,i,-1))
       # print(list_number)
        a+=''.join(str(i) for i in list_number) + "\n"
         

    return a
        
        
#         lst.append(k)
#     print(lst)
    
#     a_list = list(range(1, 5))
#     #for i in range(0,len(lst)):
        
# #    a += ''.join(str(i) for i in lst[i:]) + "\n"
        
#     return a
        

print(pattern(5))

#%%
def pattern(n):
    
    return '\n'.join(str(i) * i for i in range(1, n + 1))

print(pattern(5))


#%%%

def pattern(n):
  return "\n".join(["".join([str(y) for y in range(n, x, -1)]) for x in range(n)]);

print(pattern(5))

#%%

