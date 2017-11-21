# Wildcard matching
# ?: any one char
# *:  any sequence of characters including the empty sequence

def wildCardMatch(text, pattern):
    p = len(pattern)
    t = len(text)
    table = [[False for i in xrange(p +1)] for j in xrange(t+1)]
    if p == 0:
        return t == 0
    table[0][0] = True

    # only * can match an empty string
    for i in xrange(1, p +1):
        if pattern[i-1] == '*':
            table[0][i] = True
            
    for i in xrange(1, t +1):
        for j in xrange(1, p + 1):
            if text[i-1] == pattern[j-1] or pattern[j-1] == '?':
                table[i][j] = table[i-1][j-1]
            elif pattern[j-1] == '*':
                # or ignore * and move to the next char in the pattern
                table[i][j] = table[i-1][j] or table[i][j-1]
            else:
                table[i][j] = False

    return table[t][p]

print wildCardMatch('xaylmz', 'x?y*z')
print wildCardMatch('', '?')
print wildCardMatch('t', '*')
print wildCardMatch('', '*')
