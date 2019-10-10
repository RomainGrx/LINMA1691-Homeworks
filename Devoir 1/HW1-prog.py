"""
    Students template for the first homework of LINMA1691 "Théorie des graphes".

    Authors : Philippe Matthew, Devillez Henri
"""

import itertools
import csv

#import numpy as np
#import networkx


def check_mapping(A, B, h):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - h an array describing an isomorphism mapping node i from A to node h[i] from B  
    Return True if h(A) = B, False otherwise
    """
    n = len(A)
  #  matrix = [x[:] for x in A]

    for i in range(n):
        for j in range(n):
            val = B[h[i]][h[j]]
            if (A[i][j] != val):
                return False
       #     matrix[i][j] = val

    return True


def are_iso(A,B):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        
    Return (Ans, h) with :
        - Ans = True if A and B are isomorphs, False otherwise
        - h an array describing an isomorphim such that h(A) = B
    """
    n = len(A)
    arange = range(n)
    h_possibilities = list(itertools.permutations(arange))
    
    for h in h_possibilities:
        if check_mapping(A, B, list(h)):
            return True,list(h)

    return False, []


def color_ones(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)
        
    Return an array of same dimension as A containing only ones
    """
    n = len(A)

    return [1]*n


def color_degree(A):
    """
    Input :
        - A an adjacency matrix (array of arrays)
    
    Return an array containing the degrees of the nodes of A
    """
    n = len(A)
    deg = [sum(A[i]) for i in range(n)]
    for i in range(n):
        if A[i][i]:
            deg[i] += 1
   

    return deg



def color_k_neigh(A, k):
    """
    Input :
        - A an adjacency matrix (array of arrays)
        - k the size of the neighbourhood of the coloring scheme 
    
    Return an array containing the colors as defined in Q4 of the project statement
    The colors have to be structured as a sorted tuple of pairs (k, deg(v)) 
    """
    
    degrees = [sum(A[i]) for i in range(len(A))]
    ar = []

    n = len(A)  
    Nodes = [[0]*n]*n
    
    for i in range(n):
        ar.append([])
        for j in range(k+1):
            Nodesprime = Nodes[i][:]
            if j==0:
                Nodesprime[i]=1
            else:
                for m in range(n): 
                    if(Nodes[i][m]==1):
                        for p in range(n):
                            if(A[m][p]==1):
                                Nodesprime[p]=1

            Nodes[i] = Nodesprime
        
            for o in range(n):
                if(Nodes[i][o]==1):
                    ar[i].append((j,degrees[o]))
                            


    rep = [];
    for i in range(len(ar)):
        rep.append(tuple(sorted(ar[i])))
    
    return rep    

        
def are_iso_with_colors(A, B, color = color_ones):
    """
    Input :
        - A, B two adjacency matrices (arrays of arrays) with same dimensions
        - color a coloring function
    Return (Ans, h) using the coloring heuristic with :
        - Ans = True if A and B are isomorphic, False otherwise
        - h describe an isomorphim such that h(A) = B if Ans = True, h = [] otherwise
    
    """
    colA = color(A)
    colB = color(B)
        
    def isom_color(A,B,h,count): 
    
        if (count==n and check_mapping(A,B,h)):       
            return True      
        
        else:  
            for j in range(count,n):
                for k in range(n):
                    if(k not in h):
                        if(colA[j]==colB[k]):
                            h[j] = k
                            count+=1
                            if isom_color(A,B,h,count):
                                return True
                            h[j] = -2
                            count-=1
                            
                return False
    
    n = len(A)
    h = [-2]*n
    
    return isom_color(A,B,h,0),h


if __name__ == "__main__":

    # Read Input

    with open('in1.csv', 'r') as fd:
        lines = list(csv.reader(fd, delimiter=','))
        n = int(len(lines)/2)

        A = []
        B = []

        for i in range(n):
            A.append([int(x) for x in lines[i]])
        
        for j in range(n, 2*n):
            B.append([int(x) for x in lines[j]])
    # Compute answer


   # are_iso, h = are_iso_with_colors(A, B, color_ones)


    # print(check_mapping(A,B,h))

    # bool_iso, h = are_iso_with_colors(A, B, color_degree)
    bool_iso, h = are_iso_with_colors(A, B, lambda x : color_k_neigh(x,2))
    print('ARE ISO :', bool_iso)
    print('H : \t', h)

    # Check results

    with open('out1.csv', 'r') as fd:
        lines = csv.reader(fd, delimiter=',')
        true_answer = int(next(lines)[0])
        
        if bool_iso != true_answer:
            if true_answer:
                print("Wrong answer: A and B are isomorphic")
            else:
                print("Wrong answer: A and B are not isomorphic")
        else:
            if bool_iso:
                if check_mapping(A, B, h):
                    print("Correct answer")
                else:
                    print("Wrong answer: incorrect mapping")


