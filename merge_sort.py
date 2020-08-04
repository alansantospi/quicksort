# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:27:03 2020

@author: Alan Santos
"""

def merge_sort(array):
    x = range(len(array))
    sort_half(array, 0, len(array) - 1, x)
    return array

def sort_half(array, start, end, x):
    if start >= end:
        return
    
    
    middle = (start + end) // 2

    sort_half(array, start, middle, x)
    sort_half(array, middle + 1, end, x)

    merge(array, start, end)

def merge(array, start, end):
    array[start: end + 1] = sorted(array[start: end + 1])