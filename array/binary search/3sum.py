#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

def threeSum(arr):
    ret = set()
    arr.sort()
    if len(arr) < 3:
        return []
    for i in range(len(arr)-2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                ret.add((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif s > 0:
                right -= 1
            else:
                left += 1
    return sorted(list(ret))


arr = [-1, 0, 1, 2, -1, -4]
print threeSum(arr)
