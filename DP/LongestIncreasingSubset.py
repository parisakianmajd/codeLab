# find the lenght of the longest increasing subsequen

def longestSub(arr):
    if len(arr)<2:
        return len(arr)
    #currentLen = 1
    maxLen = 1
    for i in xrange(1, len(arr)):
        if arr[i] > arr[i-1]:
            maxLen += 1
            #currentLen += 1
        #else:
        #    currentLen = 1
        #maxLen = max(maxLen, currentLen)

    return maxLen

def longestSubUntil(arr, i,maxLens):
    maxLen = 1
    for j in xrange(i):
        if arr[j] < arr[i]:
            maxLen = max(maxLen, maxLens[j] + 1)
    return maxLen

def longestSubDp(arr):
    maxLens = [1] * len(arr)
    for i in xrange(len(arr)):
        maxLens[i] = longestSubUntil(arr,i,maxLens)
    return max(maxLens)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print longestSub(arr)
print longestSubDp(arr)
