#   1,2,3 -> 1,3,2
#   3,2,1 -> 1,2,3
#   1,1,5 -> 1,5,1

#Solution approach
# 1. Find the largest index k such that a[k] < a[k + 1]. 
#   If no such index exists, the permutation is the last permutation.
#2. Find the largest index l such that a[k] < a[l]. 
#   Since k + 1 is such an index, l is well defined and satisfies k < l.
#3. Swap a[k] with a[l].
#4. Reverse the sequence from a[k + 1] up to and including the final element a[n]

def nextPermutation(A):
    N = len(A)
    if N == 1:
        return A 
    else:
        i = N-2
        while i >= 0 and A[i] >= A[i+1]:
            i -= 1
        if i == -1:
            return A[::-1]
        else:
            for j in range(N-1, i, -1):
                if A[j] > A[i]:
                    break
            A[i], A[j] = A[j], A[i]
            a, b = i+1, N-1
            while a < b:
                A[a], A[b] = A[b], A[a]
                a += 1
                b -= 1
        return A 

def nextPermutation2(arr):
    i = len(arr) - 2
    while not (i < 0 or arr[i] < arr[i+1]):
        i -= 1
    if i < 0:
        return sorted(arr)
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]        
    arr[i+1:] = reversed(arr[i+1:])  
    return arr


A= [1, 2, 3, 4]
print nextPermutation(A)
A= [1, 2, 3, 4]
print nextPermutation2(A)
