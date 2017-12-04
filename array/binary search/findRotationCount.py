#Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#Find the minimum element.

# Note: If you know the number of times the array is rotated, then this problem becomes trivial.
#If the number of rotation is x, then minimum element is A[x].

# number of rotations= index of min element

def findRotationCount(arr):
    n = len(arr)
    low, high = 0, n-1
    while low <= high:
        # if the segment is sorted return the index of the smallest element
        if arr[low] <= arr[high]:
            return low
        mid = (low + high)/2
        nextElem = (mid + 1) %n
        prevElem = (mid  + n - 1)%n
        if arr[mid] <= arr[nextElem] and arr[mid] <= arr[prevElem]:
            return mid
        # discard one of the halfs
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
arr = [ 40342, 40766, 41307, 42639, 42777, 46079, 47038, 47923, 48064, 48083, 49760, 49871, 51000, 51035, 53186, 53499, 53895, 59118, 60467, 60498, 60764, 65158, 65838, 65885, 65919, 66638, 66807, 66989, 67114, 68119, 68146, 68584, 69494, 70914, 72312, 72432, 74536, 77038, 77720, 78590, 78769, 78894, 80169, 81717, 81760, 82124, 82583, 82620, 82877, 83131, 84932, 85050, 85358, 89896, 90991, 91348, 91376, 92786, 93626, 93688, 94972, 95064, 96240, 96308, 96755, 97197, 97243, 98049, 98407, 98998, 99785, 350, 2563, 3075, 3161, 3519, 4176, 4371, 5885, 6054, 6495, 7218, 7734, 9235, 11899, 13070, 14002, 16258, 16309, 16461, 17338, 19141, 19526, 21256, 21507, 21945, 22753, 25029, 25524, 27311, 27609, 28217, 30854, 32721, 33184, 34190, 35040, 35753, 36144, 37342 ]
print (min(arr))
print arr[findRotationCount(arr)]
