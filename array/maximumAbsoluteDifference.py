#You are given an array of N integers, A1, A2 ,..., AN. Return maximum value of f(i, j) for all 1 <= i, j <= N.
#f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# Solution: expanding f(i,j) = |A[i] - A[j]| + |i - j|, gives 4 cases:
# a) (A[j]-j)-(A[i]-i)
#b) (A[j]+j)-(A[i]+i)
#c) (A[i]+i)-(A[j]+j)
#d) (A[i]-i)-(A[j]-j)
# a and d, as well as, b and c are similar
# calculate the max and min for each case

def maxArr(A):
    n = len(A)
    max1= max2 = ans = -sys.maxint
    min1 = min2 = sys.maxint
    for i in xrange(n):
        max1 = max(max1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min1 = min(min1, A[i] + i)
        min2 = min(min2, A[i] - i)
    ans = max(ans, (max2 - min2))
    ans = max(ans, (max1 - min1))
    return ans
