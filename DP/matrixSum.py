#fix the left and right col one by one
#find top and bottom row numbers through Kadane algorithm
# the array temp is used to store the sums,e.g., temp[i] shows elements from left to right in row i
def findKadaneResult(arr):
    maxVal = 0
    maxStart = -1
    maxEnd = -1
    currentStart = 0
    currentMax = 0
    for i in xrange(len(arr)):
        currentMax += arr[i]
        if currentMax < arr[i]:
            currentMax = arr[i]
            currentStart = i + 1
        if currentMax > maxVal:
            maxVal = currentMax
            maxStart = currentStart
            maxEnd = i
    return {'maxVal':maxVal , 'maxStart': maxStart, 'maxEnd': maxEnd}

def findMaxSum(matrix):
    maxSum = 0
    leftBound = 0
    rightBound = 0
    upBound = 0
    lowBound = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for left in xrange(cols):
        temp = [0 for _ in xrange(rows)]
        for right in xrange(left,cols):
            for i in xrange(rows):
                temp[i] += matrix[i][right]
            kadaneResult = findKadaneResult(temp)
            if kadaneResult['maxVal'] > maxSum:
                maxSum = kadaneResult['maxVal']
                leftBound = left
                rightBound = right
                upBound = kadaneResult['maxStart']
                lowBound = kadaneResult['maxEnd']
    return maxSum, leftBound, rightBound, upBound, lowBound



    
    
matrix= [[1, 2, -1, -4, -20],\
        [-8, -3, 4, 2, 1],\
        [3, 8, 10, 1, 3],\
        [-4, -1, 1, 7, -6]]

print findMaxSum(matrix)

