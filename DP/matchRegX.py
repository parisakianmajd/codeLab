# Given a pattern consisting of characters and two special characters * and .
# and a string, find if the string matches the pattern
# e.g. bty matches a*b.*y   

def matchRegx_recursive(text,pattern, pos1, pos2):
    # if pos2 has reached the end of pattern, pos1 must have reached the end of text
    if pos2 == len(pattern):
        return pos1 == len(text)
    
    # if next character is not *, or we are one to the last char of the pattern,
    # the current value at pattern and text should be same
    # or the current value at pattern should be . in which case you can skip one character of text
    
    if pos2 == len(pattern) - 1 or pattern[pos2 + 1] != '*':
        return (pos1 < len(text) and (text[pos1] == pattern[pos2] or pattern[pos2] == '.')) and \
              matchRegx_recursive(text, pattern, pos1 + 1, pos2 + 1)
        # the next char is *
    if matchRegx_recursive(text, pattern, pos1, pos2 + 2):
        return True
    #abbc and ab*c match first b with b* and then next b to c. If that does not work out
    # then try next b with b* and then c with c and so on.
    while(pos1 < len(text) and (text[pos1] == pattern[pos2] or pattern[pos2] == '.')):
            if  matchRegx_recursive(text, pattern, pos1 + 1, pos2 + 2):
                return True
            pos1 += 1
    return False

def matchRegex(text, pattern):
    t = len(text)
    p = len(pattern)
    table = [[False for i in xrange(p + 1)] for j in xrange(t + 1)]
    table[0][0] = True

    # for a* or a*b* patterns
    for i in xrange(1, p):
        if pattern[i-1] == '*': 
            table[0][i] = table[0][i-2]

            
    for i in xrange(1, t+1):
        for j in xrange(1, p+1):
            if pattern[j-1] == text[i-1] or pattern[j-1] == '.':
                table[i][j] = table[i-1][j-1]
            elif pattern[j-1] == '*':
                table[i][j] = table[i][j-2]
                if text[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    table[i][j] = table[i][j] or table[i-1][j]
                    
            else:
                table[i][j] = False
    for tb in table:
        print tb
    return table[t][p]

text = 'xaabyc'
pattern = 'xa*b.c'
print matchRegex(text, pattern)
print matchRegx_recursive(text, pattern, 0, 0)
print matchRegx_recursive('bty', 'a*b.*y', 0, 0)
