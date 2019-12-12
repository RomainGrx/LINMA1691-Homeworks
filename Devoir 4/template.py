"""
    Solution for the fourth homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math

def matching(T, friends, hiding_places):
    """
    INPUT :
        - T, the number of seconds
        - friends, a list of tuples (x, y, v) describing the position (x, y) and velocity v
          of each friend
        - hiding_places, a list of tuple (x, y) giving the position (x, y) of each hiding place
    OUTPUT :
        - return the maximal number of friends that can hide from the game master

        See homework statement for more details
    """

    def distance(friend, mapper):
        dx = mapper[0] - friend[0]
        dy = mapper[1] - friend[1]
        return math.sqrt(dx*dx + dy*dy)

    def time(friend, mapper):
        d = distance(friend, mapper)
        velocity = friend[2]
        return d/velocity

    def accesible_times(T, friends, places):
        accesible_places = []
        times = []
        for friend in friends:
            friend_accesible_places = []
            friend_times = []
            for mapper in places:
                friend_times.append(time(friend,mapper))
                friend_accesible_places.append(friend_times[-1]<=T)
            times.append(friend_times)
            accesible_places.append(friend_accesible_places)
        return times, accesible_places

    def mapping(nplaces,acci):
        mapper = 0
        still_available = nplaces
        for iplace in range(nplaces):
            somme = 0
            for i in range(len(acci)):
                somme += acci[i]
            if(acci[iplace]):
                if somme>=still_available:
                    continue
                else:
                    mapper = iplace
                    still_available = somme

        return mapper, still_available

    ret = 0
    nfriends = len(friends)
    nplaces  = len(hiding_places)
    times, accesible_places = accesible_times(T, friends, hiding_places)

    available = 1
    while True:
        ifriend = 0
        while True:
            somme = 0
            for i in range(len(accesible_places[ifriend])):
                somme += accesible_places[ifriend][i]
            if somme is not available:
                ifriend +=1
                if(nfriends<= ifriend):
                    break
            else:
                mapper, still_available = mapping(nplaces,accesible_places[ifriend])
                ret += 1
                if(nfriends<=0):
                    break
                accesible_places[ifriend] = [False]*nplaces
                for k in range(nfriends):
                    accesible_places[k][mapper] = False
                ifriend = 0
                available = 1
        available += 1
        if(available>nplaces):
            break

    return ret


if __name__ == "__main__":

    # Read Input

    with open('in2.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')

        n, m, T = int(l[0]), int(l[1]), int(l[2])

        friends = []
        for friend in range(n):
            l = fd.readline().rstrip().split()
            friends.append(tuple([float(x) for x in l]))

        hiding_places = []
        for hiding_place in range(m):
            l = fd.readline().rstrip().split()
            hiding_places.append(tuple([float(x) for x in l]))

    # Compute answer

    ans = matching(T, friends, hiding_places)
    print(ans)

    # Check results

    with open('out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans:
            print("Test sample : Correct")
        else:
            print("Test sample : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output))
