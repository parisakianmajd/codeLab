#Find Index of 0 to be replaced with 1 to get longest continuous sequence of 1s in a binary array
# we need to find a 0 with max number of 1s around it


# Time complexity O(n)

def maxOnesIndex(arr):
    maxCount = 0 # max number of 1s around a 0
    prevZero = -1  #index of previous zero
    prevToPrevZero = -1 # index of previous to previous zero

    for i in xrange(len(arr)):
        if arr[i] == 0:
            # number of 1s around
            ones = i - prevToPrevZero
            if ones > maxCount:
                maxCount = ones
                maxIndex = prevZero
            
            prevToPrevZero = prevZero
            prevZero = i
    # if this is the last zero
    if len(arr) - prevToPrevZero > maxCount:
        maxIndex = prevZero
    return maxIndex

        
arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
print maxOnesIndex(arr)
