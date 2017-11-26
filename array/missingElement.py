from collections import defaultdict
# There are two arrays of non-negative integers. The second array is formed by shuffling
# the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.

def findMissing1(arr1, arr2):
    #return set(arr1) ^ set(arr2)
    return reduce(lambda x,y: x^y, arr1+arr2)


def findMissing2(arr1, arr2):
    d = defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        d[num] -= 1

    
def findMissing3(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for a, b in zip(arr1,arr2):
        if a != b:
            return a
    return arr1[-1]


arr1 = [4,1,0,2,9,6,8, 7,5,3]
arr2 = [6,4,7,2,1,0,8,3,9]

print findMissing1(arr1, arr2)
print findMissing2(arr1, arr2)
print findMissing3(arr1, arr2)
