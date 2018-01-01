#Given an array (zero indexed) of N non-negative integers, A0, A1, ..., AN-1.
#Find the minimum sub array Al, Al+1, ..., Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
#If A is already sorted, output -1.

#Solution: Assume that Al, ...,  Ar is the minimum-unsorted-subarray which is to be sorted.
#then min(Al, ...,  Ar) >= max(A0, ...,  Al-1)
#and max(Al, ...,  Ar) <= min(Ar+1, ..., AN-1)

def subUnsort(A):
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


A = [1, 3, 2, 4, 5]
print subUnsort(A)
