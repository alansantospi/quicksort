# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:42:27 2020

@author: Alan Santos
"""

import random
import time
import sys
import numpy as np
import pandas as pd

vetor = list(range(0,1000)) #gera vetor
random.shuffle(vetor)
print(vetor)

vq = vetor.copy() #Quick Sort

#Quick Sort Variante Lomuto (pivo extrema esquerda)
def quick_sort(vq, p, r, t):
    if p < r: #Condicao de Parada (ou condicao de existencia)
        if t: 
            q = lomuto(vq, p, r)
        else: 
            q = hoare(vq, p, r)
        quick_sort(vq, p, q-1, t) #Pivotar a Esquerda (Ordenar os elementos menores do que o Pivô)
        quick_sort(vq, q+1, r, t) #Pivotar a Direita (Ordenar os elementos maiores do que o Pivô)

def lomuto(vq, p, r):
    x = vq[p] #Escolhendo o Pivo (É o primeiro elemento da esquerda)
    i = p #Destino final do Pivô
    j =  p + 1 #Contador para percorrer o restante do vetor

    while j <= r: #Percorrer o vetor
        if vq[j] < x: #detectou-se um elemento menor que o pivô, incrementa o i
            i += 1
            swap(vq, i, j)
        j += 1 #passa para o proximo elemento

    swap(vq, p, i)

    return i

def hoare(a, p, r):
  x = a[p]
  i, j = p-1, r+1
  while True:
    while True:
      j -= 1
      if a[j] <= x:
        break
    while True:
      i += 1
      if a[i] >= x:
        break
    if i < j:
      a[i], a[j] = a[j], a[i]
    else:
      return j

def swap(vq, n, m):
    temp = vq[n]
    vq[n] = vq[m]
    vq[m] = temp
    
    
randomList = []
# Set a length of the list to 10
for i in range(0, 10):
    # any random numbers from 0 to 1000
    randomList.append(random.randint(0, 1000))

print("Printing list of 10 random numbers")
print(randomList)

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
    
def test(min, max, rep, tam, t):
    #matrix={}
    array = []
    for n in tam:
        i = 0
        r = []
        print(n)
        while i<rep:
            vetor = randIntList(min, max, n)
            random.shuffle(vetor)
            before = time.time()
            quick_sort(vetor, 0, len(vetor)-1, t)
            after = time.time()
            
            total = (after - before)*1000
            #print("Quick Sort %0.2f ms" %total)
            r.append(total)
            i = i + 1
        m = np.mean(r)
        array.append(m)   
        #matrix[n]=[m]
    return array
        
min = 0 # int(-sys.maxsize - 1)
max = int(sys.maxsize) #9223372036854775807
rep = 100
tam = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]

hoare = test(min, max, rep, tam, False)
lomuto = test(min, max, rep, tam, True)

df = pd.DataFrame({'Hoare': hoare, 'Lomuto': lomuto}, index=tam)
ax = df.plot.bar(rot=0)
fig = ax.get_figure()
fig.savefig('/figure.pdf')    
    



