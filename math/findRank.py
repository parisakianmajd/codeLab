#Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
#Note that the characters might be repeated. 

from collections import defaultdict

def findRank(perm):
    rank = 1
    previousPerms = 1
    ctr = defaultdict(int)
    for i in range(len(perm)):
        x = perm[((len(perm) - 1) - i)]
        ctr[x] += 1
        for y in ctr:
            if (y < x):
                rank += ((previousPerms * ctr[y]) // ctr[x])
        previousPerms = ((previousPerms * (i + 1)) // ctr[x])
    return rank


def findRank2(A):
    if len(A) == 0:
        return 1
    l = list(A)
    chars = sorted(l)
    if chars == l:
        return 1
    
    dic = {}
    length = len(A)
    sums = 0
    index = -1
    
    def factorial(num):
        fact = 1
        for i in range(1 , num+1):
            fact = fact*i
        return fact
    
    i = 0
    
    while i < len(chars):
        if chars[i] == l[i]:
            i += 1
            continue
        else:
            for j in range(i+1 , len(chars)):
                if chars[j] in dic:
                    dic[chars[j]] += 1
                else:
                    dic[chars[j]] =1
                
                if index == -1 and chars[j] > chars[i]:
                    index = j
            
            val = factorial(length-i-1)    
            for key , item in dic.iteritems():
                if item >= 2:
                    val = val/factorial(item)
            
            sums += val
            dic = {}    
            chars[i] , chars[index] = chars[index] , chars[i]
            chars = chars[:i+1] + sorted(chars[i+1:])
            index = -1



perm = 'abaab'
print findRank(perm)
