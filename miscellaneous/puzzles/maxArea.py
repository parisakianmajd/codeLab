#Given n non-negative integers a1, a2, ..., an,
#where each represents a point at coordinate (i, ai).
#'n' vertical lines are drawn such that the two endpoints of line i is
#at (i, ai) and (i, 0).

#Find two lines, which together with x-axis forms a container,
#such that the container contains the most water.

#When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
#  The base (N-1) is the maximum possible.
# Thus, if there is any better solution the min has to be higher. =>
# move the pointers to discard the min of a1, aN

def maxArea(A):
    maxArea = 0
    left = 0
    right = len(A) - 1
    while left < right:
        area = (right - left) * min(A[right], A[left])
        if area > maxArea: 
            maxArea = area
        if A[right] < A[left]:
            right -= 1
        else:
            left += 1
    return maxArea

A = [1, 5, 4, 3]
print maxArea(A)
