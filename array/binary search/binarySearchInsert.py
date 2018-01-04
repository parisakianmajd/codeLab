# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

def searchInsert(A, B):
    if len(A) < 1:
        return 0
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high-low)/2
        if A[mid] == B:
            return mid
        elif A[mid] > B:
            high = mid - 1
            pos = mid
        else:
            low = mid + 1
            pos = low
    return pos


A = [1,3,5,6]
B = 7
print searchInsert(A, B)
