# Find two lines, which together with x-axis forms a container, such that the container contains
# the most water.

# Input : [1, 5, 4, 3]
#Output : 6
#Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 

#Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
#Note 2: The base (N-1) is the maximum possible.
#This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).

#B * H > (N-1) * min(a1, aN)
#We know that, B < (N-1)
#So, H > min(a1, aN)

#This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.


def maxArea(arr):
    if len(arr) <= 1:
        return 0
    left = 0
    right = len(arr) - 1
    ans = 0

    while left < right:
        area = (right - left) *  min(A[left], A[right])
        ans = max(area, ans)
        if(A[left] > A[right]):
            right -= 1
        else:
            left += 1
    return ans
