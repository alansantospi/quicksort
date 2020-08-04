# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:34:41 2020

@author: Alan Santos
"""

def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b  

def insertion_sort(array):
    #x = range(len(array))
    #img_path = "C:/Users/edina/Alan/py/sort/insertion_sort/img"
    #imgidx = 0
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1
    return array