# Given three sorted arrays
# Findthe minimum absolute difference between the maximum and minimum number
#from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.

from sys import maxint
            
def maxDiff(A, B, C):
    a = b = c = 0
    if len(A) == 0 or len(B) == 0 or len(C) == 0:
        return
    minDiff = maxint
    while a < len(A) and b < len(B) and c < len(C):
        minVal = min(A[a], B[b], C[c])
        maxVal = max(A[a], B[b], C[c])
        diff = maxVal - minVal
        if diff == 0:
            minDiff = diff
            break
        if diff < minDiff:
            minDiff = diff
        if A[a] == minVal:
            a += 1
        elif B[b] == minVal:
            b += 1
        else: 
            c += 1
    return minDiff

A = [ 1, 4, 5, 8, 9 ]
B = [ 6, 9, 10 ]
C = [ 2, 3, 6, 10 ]
print maxDiff(A, B, C)
