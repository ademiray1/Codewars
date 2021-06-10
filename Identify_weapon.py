# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(irnmn)s


The characters of Chima need your help. Their weapons got mixed up! They need you to write a program that accepts the name of a character in Chima then tells which weapon he/she owns.

For example: for the character "Laval" your program should return the solution "Laval-Shado Valious"

You must complete the following character-weapon pairs:

Laval-Shado Valious,
Cragger-Vengdualize,
Lagravis-Blazeprowlor,
Crominus-Grandorius,
Tormak-Tygafyre,
LiElla-Roarburn.
  





"""
#Dictionary
#Re-organize the weapons!

def identify_weapon(character):
    #insert your code here...FOR CHIMA!
    dic = {}
    
    if character == 'laval':
        return "Laval-Shado Valious"
    if character == 'Cragger':
        return "Vengdualize"
    if character == 'Lagravis':
        return "Blazeprowlor"
    if character == 'Crominus':
        return "Grandorius"
    if character == 'Tormak':
        return "Tygafyre"
    if character == 'LiElla':
        return "Roarburn"
    
    

    

print(identify_weapon("laval"))

#%%

def identify_weapon(character):
    wep = {
    "Laval":"Laval-Shado Valious",
    "Cragger":"Cragger-Vengdualize",
    "Lagravis":"Lagravis-Blazeprowlor",
    "Crominus":"Crominus-Grandorius",
    "Tormak":"Tormak-Tygafyre",
    "LiElla":"LiElla-Roarburn"
    }
    
    return wep.get(character, "Not a character")

print(identify_weapon("mahmut"))

"""
The get() method returns the value of the item with the specified key.
"""