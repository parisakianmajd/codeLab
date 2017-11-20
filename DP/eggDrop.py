#Given some number of floors and some number of eggs,
#what is the minimum number of attempts it will take to find out from which floor egg will break.
import sys

def eggDrop(eggs, floors):
    T = [[0 for i in xrange(floors+1)] for j in xrange(eggs+1)]
    for i in xrange(1,floors+1):
        T[1][i] = i
    for e in xrange(2,eggs+1):
        for f in xrange(1,floors+1):
            T[e][f] = sys.maxint
            for k in xrange(1,f+1):
                c = 1 + max(T[e-1][k-1], T[e][f-k])
                if c < T[e][f]:
                    T[e][f] = c
    return T[eggs][floors]

def eggDrop_recursive(eggs, floors):
    if eggs == 0 or floors == 0:
        return 0
    if eggs == 1:
        return floors
    minFloors = sys.maxint
    for i in xrange(1,floors+1):
        c = 1 + max(eggDrop_recursive(eggs-1, i-1), eggDrop_recursive(eggs, floors-i))
        if c < minFloors:
            minFloors = c 
    return minFloors


print eggDrop(2,100)
print eggDrop_recursive(2,100)
