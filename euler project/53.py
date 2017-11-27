# -*- coding: utf-8 -*-
# Problem 53- How many, not necessarily distinct, values of  nCr,
# for 1 ≤ n ≤ 100, are greater than one-million?



from math import factorial

def ncr(n, r):
    return reduce(lambda x,y: x*y, range(n, n-r, -1)) / factorial(r)



# exploiting pascal triangle symmetry
def pascal():
    limit = 1000000
    nlimit = 100
    count = 0
    pascalTriangle = [[0 for i in xrange(nlimit/2 + 1)] \
                      for j in xrange(nlimit+1)]
    
    for i in xrange(nlimit +1):
        pascalTriangle[i][0] = 1

    
    for n in xrange(1,nlimit +1):
        for r in xrange(1,nlimit/2 + 1):
            pascalTriangle[n][r] = pascalTriangle[n - 1][r] +\
                                   pascalTriangle[n - 1][r-1]
            if pascalTriangle[n][r] > limit:
                count += n - 2 * r + 1
                break
    return count


# bruth force
count = 0
for n in xrange(23, 101):
    for r in xrange(1,n):
        choose = ncr(n,r)
        if choose >= 1000000:
            count += 1
print count
print pascal()
