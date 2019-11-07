"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import math
import random

class Union_Find():
    """
    Disjoint sets data structure for Kruskal's algorithm.

    It is useful to keep track of connected components (find(a) == find(b) iff they are connected).

    """

    def __init__(this, N):
        """
        INPUT :
            - N : the initial number of disjoints sets
        """
        this.N = N
        this.p = list(range(N))
        this.size = [1]*N

    def union(this, a, b):
        """
        INPUT :
            - a and b : two elements such that 0 <= a, b <= N-1
        OUTPUT:
            - return nothing

        After the operation, the two given sets are merged
        """
        a = this.find(a)
        b = this.find(b)

        if a == b:
            return

        # Swap variables if necessary
        if this.size[a] > this.size[b]:
            a,b = b,a

        this.size[b] += this.size[a]
        this.p[a] = b

    def find(this, a):
        """
        INPUT :
            - a : one element such that 0 <= a <= N-1
        OUTPUT:
            - return the root of the element a
        """
        if a != this.p[a]: this.p[a] = this.find(this.p[a])
        return this.p[a]


def spanning_tree_2(N, edges):
    """
    INPUT :
        - N the number of nodes
        - edges, list of tuples (u, v) giving an edge between u and v

    OUTPUT :
        - return an estimation of the min cut of the graph

    This method has to return the correct answer with probability bigger than 0.999
    See project homework for more details
    """
    def karger(N, edges):
        """
        INPUT :
            - N the number of nodes
            - edges, list of tuples (u, v) giving an edge between u and v

        OUTPUT :
            - return an estimation of the min cut of the graph

        See project homework for more details
        """

        min_cut = 0

        U = Union_Find(N)

        # Nombre d'arrêtes
        n = len(edges)
        # Nombre actuel d'arrêtes dans le graphe
        m = 0

        for i in range(n):
            a = edges[i][0]
            b = edges[i][1]

            if(U.find(a) != U.find(b)):
                U.union(a, b)
                m += 1

            if(m == N-2) : break

        for i in range(n):
            a = edges[i][0]
            b = edges[i][1]

            if(U.find(a) != U.find(b)):
                min_cut += 1

        return min_cut

    def randomize_edges(edges):
        """
        INPUT :
            - edges : a list of undirected edges (u, v)
        OUTPUT:
            - return a list of random weighted undirected edges (u, v, w)
        """

        return [(edges[i][0], edges[i][1],random.random()) for i in range(len(edges))]



    # TO COMPLETE (apply karger several times)
    # Probability to return the true min cut should be at least 0.9999

    edges = sorted(randomize_edges(edges), key=lambda e: e[2])
    min_cut = karger(N, edges)

    prob = 2/(N*(N-1))

    trials = math.ceil(math.log(0.0001, 1-prob))

    for i in range(trials):
        edges = sorted(randomize_edges(edges), key=lambda e: e[2])
        min_cut = min(min_cut, karger(N, edges))

    return min_cut


if __name__ == "__main__":

    # Read Input for the second exercice

    with open('../res/in2.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')

        n, m = int(l[0]), int(l[1])

        edges = []
        for edge in range(m):

            l = fd.readline().rstrip().split()
            edges.append(tuple([int(x) for x in l]))

    # Compute answer for the second exercice

    ans = spanning_tree_2(n, edges)

    # Check results for the second exercice

    with open('../res/out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output))
