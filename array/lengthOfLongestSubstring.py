#Given a string, 
#find the length of the longest substring without repeating characters.

#Example:

#The longest substring for A= "abcabcbb" is "abc", which the length is 3.
#For "bbbbb" the longest substring is "b", with the length of 1.

def lengthOfLongestSubstring2(A):
    maxLen= 0
    visited = {}
    n = len(A)
    i = 0
    j = 0
    
    while j < n:
        if A[j] not in visited:
            visited[A[j]] = 1
            maxLen = max(maxLen , len(visited))
            j += 1
        else:
            while True:
                del visited[A[i]]
                if A[i] == A[j]:
                    i += 1
                    break
                else:
                    i += 1
    return maxLen
def lengthOfLongestSubstring(A):
    visited = {}
    currentLen = 0
    i = 0
    maxLen = 0
    start = 0
    while i < len(A):
        if A[i] in visited:
            if visited[A[i]] >= start:
                currentLen = i - start
                start = visited[A[i]] + 1
                maxLen = max(maxLen, currentLen)
        visited[A[i]] = i
        i += 1
    maxLen = max(maxLen, i - start)
    return maxLen
