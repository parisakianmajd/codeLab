#You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

#Find i, j, k such that :
#max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
#Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))



import sys
def minimize(A, B, C):
    i, j, k = 0, 0, 0
    a = len(A)
    b = len(B)
    c = len(C)
    minDiff = sys.maxint
    while i < a and j < b and k < c:
        minVal = min(A[i], B[j], C[k])
        maxVal = max(A[i], B[j], C[k])
        currentDiff = maxVal - minVal
        if currentDiff < minDiff:
            minDiff = currentDiff
        if minDiff == 0:
            break
        if A[i] == minVal:
            i += 1
        elif B[j] == minVal:
            j += 1
        else:
            k += 1
        print i, j, k
    return minDiff


A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]

print minimize(A,B,C)
