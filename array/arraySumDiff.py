# To find the pairs that sum up to k, use two pointers at the start and end of array
# o find the pairs with differerence of k, use two pointers at the start of the array

#Given an integer array, output all pairs that sum up to a specific value k.
def pairSum(arr, k):
    if len(arr) < 2:
        return
    pairs = []
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < k:
            left += 1
        elif arr[left] + arr[right] > k:
            right -= 1
        else:
            pairs.append([arr[left], arr[right]])
            left += 1
    return pairs


#Given an integer array, output all triples that sum up to a specific value k.
def tripleSum(arr, k):
    triples = []
    if len(arr) < 2:
        return
    for i in xrange(len(arr)-2):
        pairs = pairSum(arr[i+1:], k - arr[i])
        if pairs is not None:
            for p in pairs:
                if arr[i] not in p:
                    triples.append([arr[i]] + p)
    return triples

# Given an integer array and a positive integer k, find all distinct pairs with differene of k
def pairDiff(arr, k):
    if len(arr) < 2:
        return
    arr.sort()
    pairs = []
    left, right = 0, 0
    while right < len(arr):
        if arr[right] - arr[left] == k:
            pairs.append([arr[left], arr[right]])
            left += 1
            right += 1
        elif arr[right] - arr[left] > k:
            left += 1
        else:
            right += 1
    return pairs
arr = [1, 5, 7, -1]
arr.sort()
k = 6
print pairSum(arr, k)
k = 5
print tripleSum(arr, k)

arr2 = [1, 5, 3, 4, 2]
print pairDiff(arr2, 3)
