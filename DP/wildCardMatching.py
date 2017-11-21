# Wildcard matching
# ?: any one char
# *:  any sequence of characters including the empty sequence



def wildCardMatch_recursive(text, pattern, pos1, pos2):
    if len(text) == 0 and len(pattern) == 0:
        return True

    if len(pattern) > 1 and pattern[0] == '*' and  len(text) == 0:
        return False
 
    if (pattern[0] == '?' and len(text)! =0) or (len(text) != 0 and text[0] == pattern[0]):
        return wildCardMatch_recursive(text[1:], pattern[1:]);
 
    # with the * there are two posibilities
    if len(text) !=0 and pattern[0] == '*':
        return wildCardMatch_recursive(text[1:],pattern) or wildCardMatch_recursive(text,pattern[1:])
 
    return False

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
print wildCardMatch_recursive('xaylmz', 'x?y*z', 0, 0)
