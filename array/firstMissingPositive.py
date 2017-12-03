#Given an unsorted integer array, find the first missing positive integer.

# Solution: traverse the array of positive numbers and to mark presence of an element x,
# change the sign of value at index x to negative.
# traverse the array again and print the first index which has positive value

# seperate negative integers
def segregate(arr):
    j = 0
    for i in xrange(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j

def findMissingPositive(arr):
    print arr
    for i in xrange(len(arr)):
        if abs(arr[i]) - 1 < len(arr) and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    # return index of the first positive element
    for i in xrange(len(arr)):
        if arr[i] > 0:
            return i + 1
    return len(arr) + 1

def findMissing(arr):
    shift = segregate(arr)
    return findMissingPositive(arr[shift:])
 
    

# not efficient
def missingElement(arr):
    for i in xrange(len(arr)):
        if arr[i] > 0:
            for i in xrange(1, arr[i]):
                if i not in arr:
                    return i
    if arr[-1] > 0:
        return arr[-1] + 1
    return 1
    

print missingElement([3,4,-1,1])
print missingElement([-8, -7, -6])
print missingElement([1])
print missingElement([1, 2, 3, 4, 5, 6 ])
print findMissing([-1, 1, 2, 3, 4, 5, 6])
print findMissing([3,4,-1,1,2,6,8])
