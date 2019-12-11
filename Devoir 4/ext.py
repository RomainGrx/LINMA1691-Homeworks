import math

def matching(T, friends, hiding_places):

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
        return (times, accesible_places)

    ret = 0
    nfriends = len(friends)
    nplaces  = len(hiding_places)
    times, accesible_places = accesible_times(T, friends, hiding_places)

    available = 1
    while available <= nplaces:
        ifriend = 0
        while ifriend < nfriends:
            if sum(accesible_places[ifriend]) is available:
                mapper = 0
                still_available = nplaces
                for iplace in range(nplaces):
                    s = sum(accesible_places[ifriend])
                    if accesible_places[ifriend][iplace] and s < still_available:
                        mapper = iplace
                        still_available = s
                ret += 1
                accesible_places[ifriend] = [False]*nplaces
                for k in range(nfriends):
                    accesible_places[k][mapper] = False
                ifriend = 0
                available = 1
            else:
                ifriend += 1
        available += 1

    return ret
