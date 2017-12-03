#Given a number N, return a sorted list of all factors of N.
import math

def allFactors(A):
    startFactors = []
    endFactors = []
    for i in xrange(1, int(A ** 0.5) + 1):
        if A % i == 0:
            startFactors.append(i)
            if i != A ** 0.5:
                endFactors.append(A/i)
    return startFactors + endFactors[::-1]

# Faster
def allFactors2(A):
    ans = []
    for i in range(1,int(math.sqrt(A))+1):
        if A%i==0:
            ans.append(i)
            j = A//i
            if j not in ans:
                ans.append(j)
    ans.sort()
    return ans
