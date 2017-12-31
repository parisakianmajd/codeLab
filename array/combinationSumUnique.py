#Given a collection of candidate numbers (C) and a target number (T),
#find all unique combinations in C where the candidate numbers sums to T.
#Each number in C may only be used once in the combination.

def combinationSum(A, target):
    A.sort()
    ans = set()
    
    def combinationSumHelper(arr, currentSum, index):
        if currentSum == target:
            ans.add(tuple(arr))
        elif currentSum > B:
            return 
        else:
            for i in xrange(index , len(A)):
                combinationSumHelper(arr + [A[i]], currentSum + A[i], i+1)
    
    combinationSumHelper([], 0, 0)
    return list(ans)

A = [10,1,2,7,6,1,5]
target = 8
print combinationSum(A, target)
