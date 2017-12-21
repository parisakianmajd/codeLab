#ou are given an array of N positive integers, A1, A2 ,..., AN.
# Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 1 <= i, j <= N.

import math

def cntBits(arr):
    n = len(arr)
    bits = int(math.log(max(arr) + 1, 2)) + 1
    
    result = 0
    for shift in range(bits):
        ones = 0
        for number in arr:
            ones += (number >> shift) & 1
        result += 2 * ones * (n - ones)   
    return result

A = [ 1, 3, 5 ]
print cntBits(A)
