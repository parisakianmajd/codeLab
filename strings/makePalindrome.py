# Minimum Characters required to make a String Palindromic
# e.g. Input: AACECAAAA
#Output: 2


def createLPS(A):
    M=len(A)
    lps = [None]*M
    l=0
    lps[0]=l
    i=1
    
    while i<M:
        if A[i]==A[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
    return lps
    
    
def makePalind(A):
    lps = createLPS(A+"$"+A[::-1])
    return len(A) - lps[-1]


def makePalind2(self, A):
    if A == A[::-1]:
        return 0
    j = len(A) - 1
    while j >= 0:
        B = A[:j]
        if B == B[::-1]:
            return len(A) - j
        j -= 1
    return len(A) - 1

def isPalindrome(A):
    return A == A[::-1]
def makePalind_recur(A):
    # remove chars from begining of the string and check if the result is palindrome
    if isPalindrome(A):
        return 0
    return 1 + makePalind_recur(A[:-1])
