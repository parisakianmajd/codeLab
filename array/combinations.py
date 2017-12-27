import itertools
def combine(n, k):
    if k > n:
        return []
    
    ans = []
    arr = range(1, n+1)
    
    def combineHelper(k , i , res):
        if k == 0:
            ans.append(res)
        else:
            for j in range(i+1 , len(arr)):
                combineHelper(k-1 , j, res+[arr[j]])
    
    combineHelper(k , -1 , [])
    return ans

def combine2(n, k):
    A = range(1,n+1)
    return itertools.combinations(A, k)
