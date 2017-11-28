#Each bulb has a switch associated with it, however due to faulty wiring,
#a switch also changes the state of all the bulbs to the right of current bulb.

#not efficient
def switchOn(bulbs):
    count = 0
    i = 0
    while i < len(bulbs):
        print i
        if bulbs[i] == 0:
            count += 1
            for b in xrange(i, len(bulbs)):
                bulbs[b] ^= 1
        print bulbs
        i += 1
    return count

def bulbs(bulbs):
    switch = 0
    for bulb in bulbs:
        if (bulb + switch) % 2 == 0:
            switch += 1
    return switch

arr = [1, 1, 0, 0, 1, 1, 0, 0, 1]
#arr =[ 1, 0, 1, 0]
print bulbs(arr)
