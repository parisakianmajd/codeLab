from collections import Counter
#Given a sorted array of integers, find the number of occurrences of a given target value.
# using Binary search
# find the first and last occurance of the element in the array and the number of occurances =last - first + 1


def BinarySearch(arr, target):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) / 2
        print mid
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid -1
        else:
            return mid
    return -1

#Binary search to find the first and last occurance
def BinarySearchFirst(arr, target, searchFirst):
    low = 0
    high = len(arr)-1
    result = -1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid -1
        else:
            result = mid
            if searchFirst:
                high = mid - 1
            else:
                low = mid + 1
    return result

def findCount(arr, target):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == target:
            return 1
        else:
            return -1
    start = BinarySearchFirst(arr, target, True)
    end = BinarySearchFirst(arr, target, False)
    if start == -1 and end == -1:
        return end - start + 1


arr = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
target = 10
count = Counter(arr)
if target in count:
    print count[target]
else:
    print -1
print findCount(arr, target)
