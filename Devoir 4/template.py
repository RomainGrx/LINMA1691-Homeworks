"""
    Solution for the fourth homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import ext

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
    def distance(friend, place):
        dx = place[0] - friend[0]
        dy = place[1] - friend[1]
        return math.sqrt(dx*dx + dy*dy)

    def time(friend, place):
        d = distance(friend, place)
        velocity = friend[2]
        return d/velocity

    def accesible_times(T, friends, places):
        accesible_places = []
        times = []
        for friend in friends:
            friend_accesible_places = []
            friend_times = []
            for place in places:
                friend_times.append(time(friend,place))
                friend_accesible_places.append(friend_times[-1]<=T)
            times.append(friend_times)
            accesible_places.append(friend_accesible_places)
        return (times, accesible_places)


    ret = 0
    nfriends = len(friends)
    nplaces  = len(hiding_places)
    tested   = [[False]*nplaces]*nfriends
    map_place= [-1]*nplaces
    times, accesible_places = accesible_times(T, friends, hiding_places)

    def mapper(ifriend, test):
        nonlocal nfriends, nplaces, tested, map_place, times, accesible_places
        for iplace in range(nplaces):
            if accesible_places[ifriend][iplace] and not test[iplace]:
                test[iplace] = True
                if map_place[iplace]==-1 or mapper(map_place[iplace], test):
                    map_place[iplace] = ifriend
                    return True
        return False

    for ifriend in range(nfriends):
        if mapper(ifriend, tested[ifriend]):
            ret += 1

    return ret


if __name__ == "__main__":

    # Read Input

    with open('in1.txt', 'r') as fd:
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

    ans = ext.matching(T, friends, hiding_places)
    print(ans)

    # Check results

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)

        if expected_output == ans:
            print("Test sample : Correct")
        else:
            print("Test sample : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output))
