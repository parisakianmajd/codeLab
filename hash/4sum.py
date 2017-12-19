#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

#Note:
#Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
#The solution set must not contain duplicate quadruplets.


def fourSum(A, B):
    seen = {}
    A.sort()
    result = set()
    
    for i in xrange(len(A)-1):
        for j in xrange(i+1, len(A)):
            currentSum = A[i] + A[j]
            target = B - currentSum
            if target in seen:
                for prevSum in seen[target]:
                    if A[prevSum[1]] <= A[i] and i > prevSum[1]:
                        result.add((A[prevSum[0]], A[prevSum[1]], A[i], A[j]))
            if currentSum in seen:
                seen[currentSum].append((i, j))
            else:
                seen[currentSum] = [(i, j)]
    return sorted([list(item) for item in result])
