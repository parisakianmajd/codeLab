# Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.
from bisect import bisect_right 



def findMedian(A):
    minElem = min([a[0] for a in A])
    maxElem = max([a[-1] for a in A])
    target = (len(A) * len(A[0]) + 1) / 2
    while minElem < maxElem:
        mid = minElem + (maxElem - minElem) / 2
        count = 0
         
        # Find count of elements smaller than mid
        for i in xrange(len(A)):
            count += bisect_right(A[i], mid)
             
        if count < target:
            minElem = mid + 1
        else:
            maxElem = mid
    return minElem


def findMedian2(A):
    for i in range(1,len(A)):
        A[0].extend(A[i])
    A = sorted(A[0])
    return A[len(A)//2]

A = [[1, 3, 5],\
     [2, 6, 9],\
     [3, 6, 9]]

print findMedian(A)
