"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math

def third(s):
    return s[2]

def spanning_tree_1(N, roads):
    """
    INPUT :
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved

        See homework statement for more details
    """

    Es = sorted(roads,key=third)
    T = []
    P = [i for i in range(N)]

    while len(T)<(N-1):
        e = Es[0]
        del(Es[0])

        if(P[e[0]] != P[e[1]]): # is sont dans des cycles diff
            T.append(e)
            P0 = P[e[0]]
            P1 = P[e[1]]
            for i in range(len(P)):
                if(P[i] == P1):
                    P[i] = P0

        else:  # sinon ils sont dans le même cycle
            continue

    satisfaction = 0
    for x in roads:
        if x not in T:
            satisfaction += x[2]

    return satisfaction


if __name__ == "__main__":

    # Read Input for the first exercice

    with open('../res/in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')

        n, m = int(l[0]), int(l[1])

        roads = []
        for road in range(m):

            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))

    # Compute answer for the first exercice

    ans1 = spanning_tree_1(n, roads)

    # Check results for the first exercice

    with open('../res/out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output))
