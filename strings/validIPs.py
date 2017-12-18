#Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255.
#The numbers cannot be 0 prefixed unless they are 0.

import itertools

def restoreIpAddresses2(A):
    A = A.strip()
    n = len(A)
    if n > 12 and n < 4:
        return []
    ret = []
    i = 1
    while i <= 3 and i < n:
        j = i+1
        while j <= i + 3 and j < n:
            k = j + 1
            while k <= j + 3 and k < n:
                a = int(A[:i])
                b = int(A[i:j])
                c = int(A[j:k])
                d = int(A[k:])
                if (A[0] == '0' and (i > 1 or a != 0)) or \
                   (A[i] == '0' and (j > i+1 or b != 0)) or \
                   (A[j] == '0' and (k > j + 1 or c != 0)) or\
                   (A[k] == '0' and (n > k+1 or d != 0)):
                    k += 1
                    continue
                elif a <= 255 and a >= 0 and b <= 255 and b >= 0 and c <= 255 and c >= 0 and d <= 255 and d >= 0:
                    ret.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
                k += 1
            j += 1
        i += 1
    return ret

def isValid(s):
    if len(s) > 3:
        return False
    if len(s) == 3 and int(s) > 255: return False
    if len(s) == 3 and s[0] == '0': return False
    if len(s) == 2 and s[0] == '0': return False
    return True
    
def restoreIpAddresses2(A):
    if len(A) > 12 or len(A) < 4:
        return []
    res = []
    dots = itertools.combinations(range(len(A)), 3)
    for d in dots:
        if d[0] > 0 and d[2] < len(A) and d[1] >= d[0] + 1 and d[2] >= d[1] + 1:
            i1 = A[:d[0]]
            i2 = A[d[0]: d[1]]
            i3 = A[d[1]:d[2]]
            i4 = A[d[2]:]
            if isValid(i1) and isValid(i2) and\
               isValid(i3) and isValid(i4):
                res.append(i1 + '.' + i2 + '.' + i3 + '.' + i4)
    return res



print restoreIpAddresses('0100100')
print restoreIpAddresses2('0100100')

