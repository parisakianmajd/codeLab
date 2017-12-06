# Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
# i.e. find sum of bit differences in all pairs that can be formed from array elements

def hammingDistance(A):
    h = 0
    n = len(A)
    # Each integer can be represented by fixed 32 bit; for each bit count the # of integers that have that bit set
    # n- count is the number of integers with that bit not set
    for i in xrange(32):
        count = 0
        for j in xrange(n):
            if A[j] & (1 << i):
                count += 1
        h += count * (n - count) * 2
    return h
#Simple bruth Force
def hammingDistance1(self, A):
    h = 0
    for i in xrange(len(A)):
        for j in xrange(len(A)):
            h

A = [ 96, 96, 7, 81, 2, 13 ]
A=[2, 4, 6]
print hammingDistance(A)
