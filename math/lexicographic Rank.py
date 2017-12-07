# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# and vice versa

from math import factorial
from itertools import permutations


# with unique chars
def findRank(s):
    n = len(s)
    if n == 1:
        return 1
    first_char = s[0]
    character_greater = 0
    for c in s:
        if first_char > c:
            character_greater += 1
    return character_greater * factorial(n-1) + findRank(s[1:n])


 # for a string of length n, there are(n-1)! permations of length n-1
 # so the Rth permutation has the R / ((n-1)!) element as its first char

def findPermutation(rank, s):
    ref = sorted(s)
    ret = ""
    while ref:
        fact = factorial(len(ref) - 1)
        idx, rank = divmod(rank, fact)
        ret += ref.pop(idx)
    return ret


A = "DTNGJPURFHYEW"
print findRank(A)

A = 'cab'
print findRank(A)
print findPermutation(5, 'abc')


# bruth force###########
A = 'cab'
print findRank(A)
for i,x in enumerate(sorted(permutations(A))):
    print(i+1, x)
######################### 
