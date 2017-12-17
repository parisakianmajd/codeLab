from collections import defaultdict

# Given an array of strings, return all groups of strings that are anagrams.
# Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.


def anagrams(A):
    anagrams = defaultdict(list)
    for i in xrange(len(A)):
        key = ''.join(sorted(A[i]))
        anagrams[key].append(i+1)
    return sorted(anagrams.values())


def isAnagram(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    if c1 == c2:
        return True
    return False
    
def isAnagram2(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))

A =  [ "cat", "dog", "god", "tca" ]
print anagrams(A)
