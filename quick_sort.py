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

def quickSort(vetor):
    return quick_sort(vetor, 0, len(vetor)-1, True)

def quick_sort(vq, p, r, t):
    if p < r: #Condicao de Parada (ou condicao de existencia)
        if t: 
            q = lomuto(vq, p, r)
        else: 
            q = hoare(vq, p, r)
        quick_sort(vq, p, q-1, t) #Pivotar a Esquerda (Ordenar os elementos menores do que o Pivô)
        quick_sort(vq, q+1, r, t) #Pivotar a Direita (Ordenar os elementos maiores do que o Pivô)
        
    return vq

#Quick Sort Variante Lomuto (pivo extrema esquerda)
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
    
    

