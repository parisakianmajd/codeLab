#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
#Given a target value to search. If found in the array, return its index, otherwise return -1.

def search(arr, target):
    n = len(arr)
    pivot = findPivot(arr, 0, n-1)
    if pivot == -1:
        return binarySearch(A, 0, n - 1, target)

    if A[pivot] == target:
        return pivot
    
    if A[0] <= target:
        return binarySearch(A, 0, pivot-1, target)
    return binarySearch(A, pivot+1, n-1, target)

# Pivot is the only element smaller than both elements next to it
def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
     
    mid = low + (high - low)/2
     {5, 6, 7, 8, 9, 10, 1, 2, 3
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid-1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)
    
def binarySearch(arr, low, high, key):
 
    if high < low:
        return -1
         
    mid = low + (high - low)/2
     
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    return binarySearch(arr, low, (mid -1), key)


# Improved Solution. One side of the mid is always sorted
def search2 (arr, low, high, key):
    if low > high:
        return -1
     
    mid =  low + (high - low) /2
    if arr[mid] == key:
        return mid
 
    # If arr[l...mid] is sorted 
    if arr[low] <= arr[mid]:
         if key >= arr[low] and key <= arr[mid]:
            return search2(arr, low, mid-1, key)
        return search(arr, mid+1, high, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(a, mid+1, high, key)
    return search(arr, low, mid-1, key)
