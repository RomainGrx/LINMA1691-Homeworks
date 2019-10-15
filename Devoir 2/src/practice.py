"""
    Students template for the second homework of LINMA1691 "ThÃ©orie des graphes".

    Authors : Devillez Henri
"""


import queue as Q
from collections import deque

LAB_TEST   = True
SPORT_TEST = False

LAB_NUMBER   = 2
SPORT_NUMBER = 1

LAB_IN_FILE    = '../res/labyrinthe/in%d.txt' %LAB_NUMBER
LAB_OUT_FILE   = '../res/labyrinthe/out%d.txt' %LAB_NUMBER
SPORT_IN_FILE  = '../res/sport/in%d.txt' %SPORT_NUMBER
SPORT_OUT_FILE = '../res/sport/out%d.txt' %SPORT_NUMBER

WALL, PATH, START, END = '#', ".", "E", "S"



def shortest_path_1(maze):

    m = len(maze)
    n = len(maze[0][:])


    # First find coordinates for start 'E'
    def start_coord(maze):
        for i in range(1, m-1):
            for j in range(1, n-1):
                if(maze[i][j] == 'E'):
                    return (i, j)
        return None

    Start = start_coord(maze)
    if(Start == None):
        return -1

    possibilities = deque([(*Start, 0)]) # Liste les possibilités autour de chaques cases à tester avec leur longueur de chemin déjà parcouru 
    seen = {Start} # Liste toutes les cases où nous sommes déjà passés



    while possibilities:
        x, y, length = possibilities.popleft()
        box = maze[y][x]

        # Liste toutes les possibilités où il n'y pas d'issues et reviens sur la boucle sans suite puisqu'il n'y a pas de chemins 
        if(box == WALL):
            continue

        if(box == END):
            return length

        if(((x, y) in seen) and ((x, y) != Start)):
            continue

        seen.add((x, y))

        for NEW in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
            possibilities.append((*NEW, length+1))



    return -1



if __name__ == "__main__":

    if LAB_TEST:

        # Read Input for the first exercice
        
        with open(LAB_IN_FILE, 'r') as fd:
            l = fd.readline()
            l = l.split(' ')
            
            n = int(l[0])
            m = int(l[1])
            
            maze = []
            for row in range(n):
                l = fd.readline().rstrip()
                maze.append(list(l))


        print('Shortest path for maze is : ', shortest_path_1(maze))