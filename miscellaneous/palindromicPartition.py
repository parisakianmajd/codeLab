
#Given a string s, partition s such that every string of the partition is a palindrome.
#Return all possible palindrome partitioning of s.

#For example, given s = "aab",
#Return
#  [["a","a","b"],["aa","b"]]

def partition(s):
    result = []
    partitionRecu(result, [], s, 0)
    return result
    
def partitionRecu(result, cur, s, i):
    if i == len(s):
        result.append(list(cur))
    else:
        for j in xrange(i, len(s)):
            if isPalindrome(s[i: j + 1]):
                cur.append(s[i: j + 1])
                partitionRecu(result, cur, s, j + 1)
                cur.pop()
            
def isPalindrome(s):
    return s == s[::-1]

s = "aabb"
print partition(s)
