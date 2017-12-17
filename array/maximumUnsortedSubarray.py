def subUnsort(A):
    n = len(A)
    if n <= 1:
        return -1
    s = 0
    e = n - 1
    while s < n-1:
        if A[s] <= A[s+1]:
            s += 1
        else:
            break
    if  s == n - 1:
        return -1
    while e > 0:
        if A[e] >= A[e-1]:
            e -= 1
        else:
            break
    maxElem = max(A[s : e + 1])
    minElem = min(A[s: e + 1])
    for i in xrange(s):
        if A[i] > minElem:
            s = i
            break
    for i in xrange(n-1, e , -1):
        if A[i] < maxElem:
            e = i
            break

    return [s, e]

def subUnsort2(A):
    B = sorted(A)
    l = 0
    r = len(A) - 1
    while l < len(A) and A[l] == B[l]:
        l += 1
    while r >= 0 and A[r] == B[r]:
        r -= 1
    if r == -1:
        return [-1]
    else:
        return [l, r]

A = [ 4, 15, 4, 4, 15, 18, 20 ]
print subUnsort(A)
