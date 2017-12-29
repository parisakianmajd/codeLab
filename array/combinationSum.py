#Given a set of candidate numbers (C) and a target number (T),
#find all unique combinations in C where the candidate numbers sums to T.

#The same repeated number may be chosen from C unlimited number of times.

def combinationSum(arr,target):
    index, ans, temp = 0, set(), []
    combination(arr,index,target,ans,temp)
    return sorted(list(ans))
    
def combination(arr,index,target,ans,temp):
    temp_sum = sum(temp)
    if temp_sum == target:
        ans.add(tuple(sorted(temp[:])))
        return
    elif temp_sum > target:
        return
    else:
        for i in range(index,len(arr)):
            temp.append(arr[i])
            combination(arr,index,target,ans,temp)
            i+=1
            temp.pop()



def combinationSum2(A, B):
    A = sorted(list(set(A)))
    rec.ans = []
    rec(A, [], B)
    return rec.ans
    
def rec(arr, current, limit):
    if sum(current) > limit:
        return
    if sum(current) == limit:
        rec.ans.append(current)
        return
    for i in xrange(len(arr)):
        rec(arr[i:], current + [arr[i]], limit)



A = [2, 3, 6, 7]
target = 8
print  combinationSum(A,target)
print  combinationSum2(A,target)

