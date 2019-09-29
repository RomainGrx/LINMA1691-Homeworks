#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:43:16 2019

@author: francois
"""
#import numpy as np

n = 4
couleurA = [2, 3, 2, 3]
couleurB = [3, 2, 3, 2]
paires = [[-1]*2]*n*n
count = 0

for j in range(n):
    for k in range(n):
        if(couleurA[j]==couleurB[k]): #on a une paire valide
         #   print(j,k)
            count=count+1
            
A = [[0, 1, 0, 1],
     [1, 0, 1, 1],
     [0, 1, 0, 1],
     [1, 1, 1, 0]]

k = 1

degrees = [sum(A[i]) for i in range(len(A))]
#print(degrees[0])

ar = []

def calcul(nbase,noeud,w,k):
    if w==0:
        print("up")
        ar[nbase].append((k,degrees[noeud]))
    else:
        for l in range(len(A)):
           # print("ici")
            print(A[l])
            if(A[noeud][l]==1):
                print("ici")
                calcul(nbase,l,w-1,k)
            
for i in range(len(A)):            # on parcourt chaque ligne
    ar.append([])
    for j in range(k+1):           # on test tous les k 

        calcul(i,i,j,j)
        print("changing")
#    print("change")

print(ar)