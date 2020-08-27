# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s
"""


def capitals(word):
    #your code here
    
    new_list = []
    print(word)
    for i in range(len(word)):
        
      #  print(i)
        if word[i].isupper():
            
            new_list.append(i)
            
    new_list.sort()       
    return new_list
        
        
word = 'codEwARs'
print(capitals(word))



#%%
def capitals(word):
    
#    return [w for w in range(len(word)) if word[w] == word[w].upper()]
    return [w for w in range(len(word)]


#%%
def capitals(word):
    for count, x in enumerate(word):
        print(f"count={count} x = {x}")
                             
print(capitals(word))

#%%
def capitals(word):
    return [count for count, x in enumerate(word) if x.isupper()== True]


print(capitals(word))
