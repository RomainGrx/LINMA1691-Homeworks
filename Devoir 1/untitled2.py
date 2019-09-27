#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:43:16 2019

@author: francois
"""

n = 4
couleurA = [2, 3, 2, 3]
couleurB = [3, 2, 3, 2]
paires = [[-1]*2]*n*n
count = 0

for j in range(n):
    for k in range(n):
        if(couleurA[j]==couleurB[k]): #on a une paire valide
            print(j,k)
            count=count+1