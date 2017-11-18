# Minimum Edit Distance


def minEditDist_recursive(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return minEditDist_recursive(str1, str2, m-1, n-1)
    # if the last characters are not the same, consider all 3 operations
    # of insert, remove, replace and find the minimum cost
    return 1+ min(minEditDist_recursive(str1, str2,m,n-1),\
                  minEditDist_recursive(str1, str2,m-1,n),\
                  minEditDist_recursive(str1, str2,m-1,n-1))   


def minEditDist(str1, str2):
    T = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in xrange(len(str2)+1):
        T[i][0] = i
    for i in xrange(len(str1)+1):
        T[0][i] = i
    for i in xrange(1, len(str2)+1):
        for j in xrange(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = min(T[i-1][j-1], T[i-1][j], T[i][j-1]) + 1
    return T[-1][-1]


str1 = "sunday"
str2 = "saturday"
print minEditDist(str1, str2)
print minEditDist_recursive(str1, str2, len(str1), len(str2))
