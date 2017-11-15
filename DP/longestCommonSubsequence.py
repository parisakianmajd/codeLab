def longestCommonSubDp(str1, str2):
    m = len(str1)
    n = len(str2)
    counter = [[0 for i in xrange(n+1)] for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set=set()
                    longest = c
                lcs_set.add(str1[i-c+1:i+1])

    return lcs_set


print longestCommonSubDp('ABCDEOOOO', 'ABCGFOOOO')
