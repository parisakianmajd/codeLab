def maxSumIncreasingSubsequence(arr):
    maxSums = []
    seq = []
    for i in xrange(len(arr)):
        maxSums.append(arr[i])
        seq.append(i)
    for i in xrange(len(arr)):
        for j in xrange(i):
            if arr[j] < arr[i]:
                maxSums[i] = max(maxSums[i], maxSums[j] + 1)
                seq[i] = j
    return seq, maxSums[-1]


arr = [4,6,1,3,8,4,6]

seq, maxSum = maxSumIncreasingSubsequence(arr)
print seq
print maxSum
