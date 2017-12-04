# Equilibrium index of an array is an index such that the sum of elements
# at lower indexes is equal to the sum of elements at higher indexes.

# solution. 1- Find the total sum of array as the rightsum
# 2- as moving from left to righ, subtract the current num from the leftsum and add it to the right sum

# Given an array turns an equilibrium index (if any)
# or -1 if no equilibrium indexes exist.

def equilibrium(arr):
    rightSum = sum(arr)
    leftSum = 0
    for i, num in enumerate(arr):
        rightSum -= num
        if leftSum == rightSum:
            return i
        leftSum += num
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print equilibrium(arr)
