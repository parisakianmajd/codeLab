# Maximum Increasing Subsequence
# O(nlog n) solution using Binary Search

def ceilIndex(arr, T, end, s):
    # Binary Search
    start = 0
    length = end
    while(start <= end):
        middle = (start + end)/2;
        if middle < length and arr[T[middle]] < s and s <= arr[T[middle+1]]:
            return middle+1
        elif arr[T[middle]] < s:
            start = middle + 1
        else:
            end = middle - 1
    return -1
    
def longestIncreasingSubSequence(arr):
    T = [None] * len(arr)
    R = [-1] * len(arr)
    T[0] = 0
    length = 0
    for i in xrange(1, len(arr)):
        # if arr[i] is smallest among all
        if arr[T[0]] > arr[i]:
            T[0] = i
        # if arr[i] is the greatest among all
        elif arr[T[length]] < arr[i]:
                 length += 1
                 T[length] = i
                 R[T[length]] = T[length-1]
        # else find the greater element less than arr[i] 
        else:
            index = ceilIndex(arr, T, length, arr[i]);
            T[index] = i
            R[T[index]] = T[index-1]

    index = T[length]
    maxsub = []
    while(index != -1):
        maxsub.append(arr[index])
        index = R[index]
    return maxsub[::-1], length + 1
                     
arr = [3,4,-1,5,8,2,3,12, 7, 9, 10]
maxsub, length = longestIncreasingSubSequence(arr)
print maxsub
print length
