#Given an array of positive and negative numbers,
#find if there is a subarray (of size at-least one) with 0 sum.

# prefix array:
# there is a subarray with sum 0 if a prefix repeats
# or if there is a prefix of 0

#Time complexity O(n)

def subArrayZero(arr):
    sumMap = set([])
    subsetSum = 0
    for i in xrange(len(arr)):
        subsetSum += arr[i]
        if subsetSum == 0 or subsetSum in sumMap:
            return True
        sumMap.add(subsetSum)
    return False
    

arr = [1, 4, -2, -2, 5, -4, 3]
print subArrayZero(arr)
