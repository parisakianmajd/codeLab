# pancake sort
def min_test(arr):
        min_x = arr.index(min(arr))
        return min_x

def pancake_sorting(arr):
	# find the min, store it in a variable
	# loop from that element to second largest element, flip those
	# then move to next element, recursively call it but that element
	for i in range(len(arr)):
		j =  i + min_test(arr[i:])
		arr[j:] = reversed(arr[j:])
		# flip from end of list to current i
		arr[i:] = reversed(arr[i:]) 



arr = [1, 6, 3, 5, 7, 2, 8, 4]
pancake_sorting(arr)
print arr
