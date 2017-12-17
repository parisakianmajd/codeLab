# Find out the maximum sub-array of non negative numbers from an array.

def maxSet(A):
    n = len(A)
    if n == 0:
        return []
    
    start = 0
    end = -1
    maxSum = -1
    maxStart = -1
    maxEnd = -1
    index = 0
    while index < n:
        currentSum = 0
        while index < n and A[index] >= 0:
            currentSum += A[index]
            index += 1
        
        if currentSum > maxSum:
            maxSum = currentSum
            maxStart = start
            maxEnd = index - 1
        elif currentSum == maxSum:
            if end - start > maxEnd - maxStart:
                maxStart = start
                maxEnd = end
            
        while index < n and A[index] < 0:
            index += 1
            
        start = index
        
    return A[maxStart : maxEnd + 1]

A = [0, 0, -1, 0]
print maxSet(A)
