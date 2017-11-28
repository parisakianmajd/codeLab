# a binary-search based approach for finding the median of two sorted arrays
# time complexity O(log(n+m)) where n, m are size of the two arrays

import sys

def medianOfSortedArrays(arr1, arr2):
    if len(arr1) > len(arr2):
        return medianOfSortedArrays(arr2, arr1)
    m = len(arr1)
    n = len(arr2)
    if n ==0 and m==0:
        return -1
    start = 0
    end = m
    while start <= end:
        partition_1 = (start + end) / 2
        partition_2 = (n + m + 1)/2 - partition_1
        maxLeft_1 = arr1[partition_1 - 1] if partition_1 != 0 else -sys.maxint
        minRight_1 = arr1[partition_1] if partition_1 != m else sys.maxint
        maxLeft_2 = arr2[partition_2 - 1] if partition_2 != 0 else -sys.maxint
        minRight_2 = arr2[partition_2] if partition_2 != n else sys.maxint
        if maxLeft_1 <= minRight_2 and maxLeft_2 <= minRight_1:
            if (n + m) % 2 == 0:
                return (max(maxLeft_2, maxLeft_1) + min( minRight_2,  minRight_1))/2
            else: 
                return max(maxLeft_1,  maxLeft_2)
        if maxLeft_1 > minRight_2:
            end = partition_1 - 1
        else:
            start = partition_1 + 1


def median(arr):
    n = len(arr)
    if n ==0:
        return -1
    if n == 1:
        return arr[0]
    if n % 2 == 0:
        return (arr[n/2] + arr[n/2]-1)/2
    return arr[n/2]
    

# Compare the median of the two arrays of equal size
def medianOfSortedArrays2(arr1, arr2):
    n = len(arr1)
    if n ==0:
        return -1
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    if n == 2:
         return (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1])) / 2
    m1 = median(arr1)
    m2 = median(arr2)
    if m1 == m2:
        return m1
    if m1 < m2:
        if n % 2 == 0:
            return medianOfSortedArrays2(arr1[n/2-1:], arr2[:n-n/2+1])
        return medianOfSortedArrays2(arr1[n/2:], arr2[:n - n/2])
    if n % 2 == 0:
        return medianOfSortedArrays2(arr1[:n/2-1], arr2[n-n/2+1:])
    return medianOfSortedArrays2(arr1[:n/2], arr2[n - n/2:])



     
arr1 = [1,3, 8, 9, 15]
arr2 = [7, 11, 18, 19, 21, 25]
print medianOfSortedArrays(arr1, arr2)
arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
print medianOfSortedArrays(arr1, arr2)
print medianOfSortedArrays2(arr1, arr2)
arr1 = []
arr2 = [2,6,8,10]
print medianOfSortedArrays(arr1, arr2)
