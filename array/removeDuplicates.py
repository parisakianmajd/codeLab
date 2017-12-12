# Given a sorted array, remove the duplicates in place
#such that each element can appear atmost twice and return the new length.


def removeDuplicates(arr):
    count = 0
    n = len(arr)
    for i in xrange(n):
        if i< n-2 and arr[i] == arr[i+1] and arr[i] == arr[i+2]:
            continue
        else:
            arr[count] = arr[i]
            count += 1
    print arr[:count]
    return count

# remove duplicates so that each element appears only once
def removeDuplicates(A):
    count = 0
    n = len(A)
    for i in xrange(n):
        if i< n-1 and A[i] == A[i+1]:
            continue
        else:
            A[count] = A[i]
            count += 1
    return count

A = [1,1,1,2,2,2,2,2,5]
print removeDuplicates(A)
