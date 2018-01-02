#Given an array of N non-negative integers, A0, A1, ..., AN-1.
# Count the number of triangles which you can form using these array values.

def nTriang(arr):
    if len(arr) < 3:
        return 0
    arr.sort(reverse=True)
    count = 0
    for i in xrange(0, len(arr) - 2):
        third_side = arr[i]
        if third_side == 0:
            break
        j = i + 1
        k = len(arr) - 1
        while j < k:
            if arr[j] + arr[k] > third_side:
                count += k - j
                j += 1
            else:
                k -= 1
    return count 
