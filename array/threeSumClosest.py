#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
#Return the sum of the three integers.

#Assume that there will only be one solution


def threeSumClosest(A, B):
            A.sort()
            n = len(A)
            if n < 3:
                return 0
            res = float('inf')
            for i in xrange(n-2):
                    left = i+1
                    right = n-1
                    while left < right:
                            currentSum = A[i] + A[left] + A[right]
                            if abs(res - B) > abs(currentSum - B):
                                    res = currentSum
                            if currentSum == B:
                                    return B
                            if currentSum > B:
                                    right-=1
                            else:
                                    left+=1
            return res

A = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
B = -1
print  threeSumClosest(A, B)
