"""
Template for Homework 0 - LINMA1691

Author : Pierre Veldeman

September 2019
"""

def degMax(A):
    """
    - INPUT : A (list of lists) Adjacency matrix
    - OUTPUT : the biggest degree of the graph represented by A
    
    """
    n = len(A)
    print(n)
    deg = [sum(A[i]) for i in range(n)]
    for i in range(n):
        if A[i][i]:
            deg[i] += 1
    print(deg)
    return max(deg)


if __name__ == "__main__":
    A = [[1,1],[1,0]]
    B = [[0, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 0]]
    C = [[0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]]

    if degMax(B) == 3:
        print("Well done ! :-)")
    else:
        print("Wrong ansmwer :-(")
if 1:
    print('qderrezrevz')