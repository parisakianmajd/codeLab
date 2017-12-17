# Given an array of integers, find two numbers such that they add up to a specific target number.

def twoSum(A, B):        
    dic = {}
    for i in range(len(A)):
        diff = B - A[i]
        if diff not in dic:
            if A[i] not in dic:
                dic[A[i]] = i+1
        else:
            return [dic[diff], i+1]
    
    return []

A = [ 1, 1, 1 ]

B= 2
print  twoSum(A, B)
