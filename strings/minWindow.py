#Given a string S and a string T, find the minimum window in S
#which will contain all the characters in T in linear time complexity.


from collections import defaultdict
def minWindow(S, T):
    if len(S) < len(T):
        return ""

    countT = defaultdict(int)
    countS = defaultdict(int)
    for i in xrange(len(T)):
        countT[T[i]] += 1
    start = 0
    startIndex = -1
    minLen = len(S) + 1
    c = 0
    for i in xrange(len(S)):
        countS[S[i]] += 1
        #if countT[S[i]] != 0  and countS[S[i]] <= countT[S[i]]:
        if countT[S[i]] != 0 and countS[S[i]] <= countT[S[i]]:
            c += 1
        if c == len(T):
            # try to minimize the window

            while countS[S[start]] > countT[S[start]] or countT[S[start]] == 0:
                if countS[S[start]] > countT[S[start]]:
                    countS[S[start]] -= 1
                start += 1
            lenWindow = i - start + 1
            if minLen > lenWindow:
                minLen = lenWindow
                startIndex = start
    if startIndex == -1:
        return ""
    return S[startIndex : startIndex + minLen]

A = "ADOBECODEBANC"
B = "ABC"
print minWindow(A, B)
