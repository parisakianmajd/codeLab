# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# Example:
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6

def trap(A):
    n = len(A)
    # pre-compute the height of the highest and lowest bar
    # of left and right of each bar
    left = [0] * n
    right = [0] * n
    water = 0
 
    left[0] = A[0]
    for i in xrange(1, n):
        left[i] = max(left[i-1], A[i])
 
    right[-1] = A[-1]
    for i in xrange(n-2, -1,-1):
        right[i] = max(right[i+1], A[i])
 
    # the amount of water accumulated around each bar will be equal to
    # min(left[i], right[i]) - A[i] 
    for i in xrange(0, n):
        water += min(left[i],right[i]) - A[i]
 
    return water

# Stack-based
def trap2(A):
    stack = []
    i = 0
    n = len(A)
    if n == 0:
        return 0
    while i < n and A[i] == 0:
        i += 1
    water = 0
    while i < n:
        while len(stack) != 0 and A[i] >= A[stack[-1]]:
            bar = stack.pop()
            if len(stack) == 0:
                break
            water += (i - stack[-1] - 1) * (min(A[i], A[stack[-1]]) - A[bar])
        stack.append(i)
        i += 1
    return water

A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
print trap(A)
print trap2(A)
