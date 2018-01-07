# Given an array of integers,
# find the length of longest subsequence which is first increasing then decreasing.
# Example: 
# For the given array [1 11 2 10 4 5 2 1]
# Longest subsequence is [1 2 10 4 2 1]
# Return value 6


def longestSubsequenceLength(A):
    n = len(A)
    if n <= 1:
        return n
    left = [1 for i in xrange(n+1)]
    right = [1 for i in xrange(n+1)]

    for i in xrange(1, n):
        for j in xrange(i):
            if A[i] > A[j] and left[i] < left[j] + 1:
                left[i] = left[j] + 1
    for i in xrange(n-1, -1, -1):
        for j in xrange(i + 1, n):
            if A[i] > A[j] and right[i] < right[j] + 1:
                right[i] = right[j] + 1  
                
    maxLen = left[0] + right[0] - 1
    for i in xrange(1 , n):
        maxLen = max((left[i] + right[i] - 1), maxLen)      
    return maxLen
