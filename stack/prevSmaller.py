#Given an array, find the nearest smaller element G[i] for every element A[i]
#in the array such that the element has an index smaller than i.

#More formally,
#G[i] for an element A[i] = an element A[j] such that 
#    j is maximum possible AND 
#    j < i AND
#   A[j] < A[i]





# more efficient stack-based approach
def prevSmaller(arr):
    ret = [0 for i in xrange(len(arr))]
    stack = []
    if len(arr) <= 1:
        return [-1]
    for i in xrange(len(arr)):
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            ret[i] = -1
        else:
            ret[i] = stack[-1]
        stack.append(arr[i])

    return ret

# bruth force
def prevSmaller2(arr):
    ret = [0 for i in xrange(len(arr))]
    if len(arr) <= 1:
        return [-1]
    for i in xrange(len(arr)):
        r = None
        for j in xrange(i - 1, -1, -1):
            if arr[j] < arr[i]:
                r = arr[j]
                ret[i]  = r
                break
        if r is None:
            ret[i] = -1
    return ret


A = [ 34, 35, 27, 42 ]
print prevSmaller(A)
