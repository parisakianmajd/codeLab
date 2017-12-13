# Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
# Solution: note that if at a given time, you have 3 distinct element from the array, if you remove them from the array, your answer does not change.




def repeatedNumber(A,k=3):
    A = list(A)
    n = len(A)
    nums = [None]*(k-1)
    count = [0]*(k-1)
    for x in A:
        if x in nums:
            count[nums.index(x)] += 1
        else:
            if None in nums:
                temp = nums.index(None)
                nums[temp] = x
                count[temp] += 1
            else:
                for i in range(k-1):
                    count[i] -= 1
                    if count[i] == 0:
                        nums[i] = None
    for x in nums:
        if x and A.count(x) > n/k:
            return x
    return -1

A = [1, 2, 3, 1, 1]
print  repeatedNumber(A)
