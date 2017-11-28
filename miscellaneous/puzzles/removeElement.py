# Given an array and a value, remove all the instances of that value in the array. 
# Also return the number of elements left in the array after the operation

def removeElement(arr, a):
    index = 0
    arrLen = len(arr)
    for i in xrange(arrLen):
        if arr[i] != a:
            arr[index] = arr[i]
            index += 1
    return index

arr = [4, 1, 1, 2, 1, 3]
index = removeElement(arr, 1)
print arr[:index]
