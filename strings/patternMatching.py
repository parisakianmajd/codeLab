#KMP (Knuth Morris Pratt) Pattern Searching
#The Naive pattern searching algorithm doesn't work well in cases
#where we see many matching characters followed by a mismatching charactehenever we detect a mismatch (after some matches),
#we already know some of the characters in the text of next window. We take advantage of
# this information to avoid matching the characters that we know will anyway match


# we frst preprcosses the pattern to form the lps
def computeLPSArray(pat, M, lps):
    p = 0 #pointer to the previous longest prefix suffix
 
    lps[0] = 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[p]:
            p += 1
            lps[i] = p
            i += 1
        else:
            if p != 0:
                p = lps[p-1]
            else:
                lps[i] = 0
                i += 1
                
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # lps[] holds the longest prefix suffix for the pattern
    lps = [0 for i in xrange(M)]
    j = 0 # index for the pattern
 
    computeLPSArray(pat, M, lps)
 
    i = 0 # index for the text
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            # found pattern
            return str(i-j)
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 

 
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
