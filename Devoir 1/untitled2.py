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

#ar = []

#def calcul(nbase,noeud,w,k):
#    if w==0:
#        print("up")
#        ar[nbase].append((k,degrees[noeud]))
#    else:
#        for l in range(len(A)):
#           # print("ici")
#            print(A[l])
#            if(A[noeud][l]==1):
#                print("ici")
#                calcul(nbase,l,w-1,k)
            
#for i in range(len(A)):            # on parcourt chaque ligne
#    ar.append([])
#    for j in range(k+1):           # on test tous les k 

#        calcul(i,i,j,j)
#        print("changing")
#    print("change")

#print(ar)

#rep = [];
#for i in range(len(ar)):
#    rep.append(tuple(ar[i]))
#    print(tuple(ar[i]))
    
#print(rep)



ar = []

n = len(A)  
Nodes = [[0]*n]*n

for i in range(n):
  #  print("i=",i)
    ar.append([])
  #  print("ar=",ar)
    for j in range(k+1):
        Nodesprime = Nodes[i][:]
  #      print("j=",j)
        if j==0:
  #          print("ici")
            Nodesprime[i]=1
  #          print("Nodes=",Nodes)
        else:
            for m in range(n): 
  #              print("m=",m)
  #              print("Nodes[i]=",Nodes[i])
                if(Nodes[i][m]==1):
  #                  print("iciiii")
                    for p in range(n):
  #                      print("p=",p)
                        if(A[m][p]==1):
  #                          print("là")
                            Nodesprime[p]=1

        Nodes[i] = Nodesprime
   #     print("oui",Nodes)
        
        for o in range(n):
           # print("ici")
            if(Nodes[i][o]==1):
    #            print(j)
                ar[i].append((j,degrees[o]))
                            

#print(ar)

rep = [];
for i in range(len(ar)):
    rep.append(tuple(sorted(ar[i])))
    
#print(rep)
    
h = [1, 2, 3, 4, 5, 0]
#if 5 in h:
#    print("ok")    
t = [10, 20, 30, 40, 50, 60]

