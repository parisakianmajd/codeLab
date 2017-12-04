# a binary-search based approach for finding the median of two sorted arrays


# Sol. we need to partition the two array such that the number of elemenets in the right is equal to left and every element on the left is smaller than every element on the right
# e.g. x1, x2|, x3, x4, x5, x6
# y1, y2, y3, y4, y5,| y6, y7, y8
# if x2 <= y6 and y5 <= x3 ==> if size of array is even: med = (max(x3, y6) + min(x2, y5)) / 2   else  med = max(x2, y5)

# to find the partition do a binary search on the smaller array .. time complexity O(long(min(m, n))

import sys

def medianOfSortedArrays(arr1, arr2):
    if len(arr1) > len(arr2):
        return medianOfSortedArrays(arr2, arr1)
    m = len(arr1)
    n = len(arr2)
    if n ==0 and m==0:
        return -1
    start = 0
    end = m   # place end at the end of the smaller array
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
    

#If the two arrays are of equal size we can compare the median of the two m1, m2
# if  m1 == m2 we are done!
# if m1 > m2  median is from the first element of ar1 to m1 OR from m2 to last element of ar2 
# if m2 > m1 median is From m1 to last element of ar2 OR from the first element of ar2 to m2
# repeat this until the size of two subarrays is 2, then return  (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1])) / 2

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
