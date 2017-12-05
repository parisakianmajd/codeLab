# given a binary string(i.e. with characters 0 and 1)choose two indices L and R
# such that 1 <= L <= R <= N and flip the characters SL, SL+1, ..., SR. By flipping, we mean change character 0 to 1 and vice-versa.
# 

# perform ATMOST one operation such that in final string number of 1s is maximised. If you don't want to perform the operation, return an empty array. Else,
# return an array consisting of two elements denoting L and R.
#If there are multiple solutions, return the lexicographically smallest pair of L and R.

# if A is the number of 0s in a suset and B is the number of 1s, the net change in number of 1s after the flip is A - B
# Transform this problem to maximal segment sum problem by changing 0s to 1s and 1s to -1s

# Use Kadane algorithm to find a subset that maximizes this 



def flip(A):
    maxDiff = currentDiff = 0
    start = 0
    ans = None
    
    for i, a in enumerate(A):
        currentDiff += 1 if a is '0' else -1
        if currentDiff < 0:
            currentDiff = 0
            start = i + 1
            
        if currentDiff > maxDiff:
            maxDiff = currentDiff
            ans = [start, i]
    
    if ans is None:
        return []
    return map(lambda x: x+1, ans)



s = '1101'
s2 = '1101100111'
print flip(s2)
