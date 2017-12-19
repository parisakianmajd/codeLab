#Find the largest continuous sequence in a array which sums to zero.
#Example:
#Input: [1 ,2 ,-2 ,4 ,-4]
#Output: [2 ,-2 ,4 ,-4]


def lszero(A):
    sums = {}
    currentSum = 0
    start, end = 0,0
    sums[0] = 0
    for idx, a in enumerate(A,1):
        currentSum += a
        if currentSum in sums:
            if end - start < idx - sums[currentSum]:
                strt, end = sums[currentSum], idx
        else:
            sums[currentSum] = idx

    return A[strt:end] if strt != end else []


def lszero2(A):
    sums = {}
    maxLen = 0
    currentSum = 0
    start = None
    for i in xrange(len(A)):
        currentSum += A[i]
        if A[i] == 0 and maxLen == 0:
            start = i
            maxLen = 1
        if currentSum == 0:
            start = 0
            maxLen = i + 1
        if currentSum in sums:
            if i - sums[currentSum] > maxLen:
                maxLen = i - sums[currentSum] 
                start =  sums[currentSum] + 1
        else:
            sums[currentSum] = i
    if start is None:
        return []
    return A[start: start + maxLen]

A = [ -1, 20, 7, -22, 1, 21, 5, 24, -26, -16, -4, -9, 19, 8, -27, 28, 9, 8, -29, 29, 8, 9, 17, -28, 13, 20, -1, -8, -16 ]
print lszero(A)
print lszero2(A)


