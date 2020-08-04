# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:08:10 2020

@author: Alan Santos
"""
#from sort.insertion_sort import insertion_sort
from insertion_sort import insertion_sort as insertion
from merge_sort import merge_sort as merge
from quick_sort import quickSort as quick
from heap_sort import heapSort as heap

    
def bucketSort(x, func): 
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = func(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        l = len(arr[i])
        for j in range(l): 
            x[k] = arr[i][j] 
            k += 1
    return x 

  
## Driver Code 
#x = [0.897, 0.565, 0.656, 
#     0.1234, 0.665, 0.3434]  
#print("Sorted Array is") 
#print(bucketSort(x, heap)) 


import random
import time
import sys
import numpy as np
import pandas as pd
from scipy import stats


from util import randIntList

def test(min, max, rep, tam, func):
    #matrix={}
    array = []
    for n in tam:
        i = 0
        r = []
        print(n)
        while i<rep:
#            vetor = randIntList(min, max, n)
            
            vetor = np.random.uniform(min,max,(0,n))
            
            random.shuffle(vetor)
            before = time.clock()
            bucketSort(vetor, func)
            after = time.clock()
            
            total = (after - before)*1000
            #print("Quick Sort %0.2f ms" %total)
            r.append(total)
            i = i + 1
        m = np.mean(r)
        array.append(m)   
        #matrix[n]=[m]
    return array
        
#min = 0 # int(-sys.maxsize - 1)
min = 0.0
#max = int(sys.maxsize) #9223372036854775807
max = sys.float_info.max
rep = 100
tam = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
#tam = [100]

ins = test(min, max, rep, tam, insertion)
mer = test(min, max, rep, tam, merge)
hea = test(min, max, rep, tam, heap)
qui = test(min, max, rep, tam, quick)


df = pd.DataFrame({'Insertion': ins, 'Merge': mer, 'Heap': hea, 'Quick': qui}, index=tam)
#df = pd.DataFrame({'Insertion': ins}, index=tam)
ax = df.plot.bar(rot=0)
fig = ax.get_figure()
#fig.savefig('/figure.jpg)    

  
# This code is contributed by 
# Oneil Hsiao 