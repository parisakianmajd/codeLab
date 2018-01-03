#Write an efficient algorithm that searches for a value in an m x n matrix.
# Integers in each row are sorted from left to right.
#The first integer of each row is greater than or equal to the last integer of the previous row.


def searchMatrix(A, target):
    
    def binarySearch(arr):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low + (high-low)/2
            if arr[mid] == target:
                return 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return 0
    
    for a in A:
        if a[-1] >= target:
            return binarySearch(a)
    return 0

A = [[1,   3,  5,  7],\
     [10, 11, 16, 20],\
     [23, 30, 34, 50]]

print searchMatrix(A, 3)

