# wave sort a1 >= a2 <= a3 >= a4 <= a5.....

def waveSort(arr):
    arr = sorted(arr)
    # swap the adjancent elemtns
    for i in xrange(0,len(arr), 2):
        arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


arr = [1, 2, 3, 4]
print waveSort(arr)
arr = range(10)
print waveSort(arr)
