# Given an array find the maximum value from A[i] to A[i+k-1]
# in O(n)

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    max_numbers = []
    for i in xrange(len(nums)):
        #For every element, the previous 
        # smaller elements are useless
        # so remove them from the queue
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        # if i>= k remove the elements that are out of this window
        if i >= k and dq and dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            max_numbers.append(nums[dq[0]])

    return max_numbers

def maxSlidingWindow2(A, B):
    if B >= len(A):
        return [max(A)]

    start = 0
    res = []
    dq = []
    for i in xrange(len(A)):
        while len(dq) > start and A[dq[-1]] <= A[i]:
            dq.pop()
        dq.append(i)
        
        if i < B - 1:
            continue
        
        while (i - dq[start]) >= B:
            start += 1
        
        res.append(A[dq[start]])
    
    return res
print maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print maxSlidingWindow([12, 1, 78, 90, 57, 89, 56],3)
