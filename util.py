# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:00:22 2020

@author: Alan Santos
"""
import random 

# Generate 'n' unique random numbers within a range
def randIntListUnique(min, max, tam):

    randList = random.sample(range(min, max), tam)
    
    return randList

# Generate a list of random int numbers
# start = starting range, 
# end = ending range 
# num = number of
def randIntList(start, end, num): 
    
    randList = [] 
    # append generated number to a list
    for j in range(num): 
        randList.append(random.randint(start, end)) 
  
    return randList 