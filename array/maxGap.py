# Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].



import sys
def maximumGap(A):
    if len(A) <= 1:
        return 0
    LMin = [None for i in xrange(len(A))]
    RMax = [None for i in xrange(len(A))]
    LMin[0] = A[0]
    for i in xrange(1, len(A)):
        LMin[i] = min(A[i], LMin[i-1])
    RMax[-1] = A[-1]
    for i in xrange(len(A) - 2, -1, -1):
        RMax[i] = max(A[i], RMax[i + 1])
    # Traverse both arrays from left to right to find optimum j - i
    # Similar to merge process of merge sort
    i = 0
    j = 0
    maxDiff = - sys.maxint
    while j < len(A) and i < len(A):
        if LMin[i] <= RMax[j]:
            maxDiff = max(maxDiff, j- i)
            j += 1
        else:
            i += 1
    return maxDiff



def get_ans(A, stack, index):
    _len = len(stack)-1
    _value = A[index]
    rt = -1
    while _len >=0:
        if A[stack[_len]] <= _value:
            rt = index - stack[_len]
        else:
            return rt
        _len -=1
    return rt
    

def maximumGap2(A):
    if not A or len(A)==1:
        return 0
    
    stack = [0]
    ans = 0
    for i in range (1, len(A)):
        top = A[stack[-1]]
        if A[i] >= top:
            rt = get_ans(A, stack, i)
            ans = max(ans, rt)
        else:
            stack.append(i)
    return ans

A = [ -1, -1, 2 ]
print maximumGap(A)
