#Given a sorted array of integers, find the starting and ending position of a given target value.
# See also count.py for the same problem and see Python bisec approach at the end

#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].

# Two times binary search

import bisect

def findRightBorder(arr, start, end, target):
    while start < end:
        med = end - (end - start) / 2
        if arr[med] != target:
            end = med - 1
        else:
            start = med
    return start
def findLeftBorder(arr, start, end, target):
    while start < end:
        med = start +(end - start) / 2
        if arr[med] != target:
            start = med + 1
        else:
            end = med
    return start
           
def search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        med = (start + end) / 2
        if arr[med] > target:
            end = med - 1
        elif arr[med] < target:
            start = med + 1
        else:
            print med
            result = []
            result.append(findLeftBorder(arr, start, med, target))
            result.append(findRightBorder(arr, med, end, target))
            return result
    return [-1,-1]


# Bisect module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
# bisect_left: The returned insertion point i partitions the array a into two halves
# so that all(val < x for val in a[lo:i]) for the left side and similarly everything on the right side is greater than x
def searchRange(arr, target):
    start = bisect.bisect_left(arr, target)
    if start == len(arr) or arr[start] != target:
        start = end = -1
    else:
        end = bisect.bisect_right(arr, target) - 1
    return [start, end]



A =  [5, 7, 7, 8, 8, 10]
print search(A, 8)
print searchRange(A, 8)
