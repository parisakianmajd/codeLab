def compareVersion(v1, v2):
    v1 = map(int, v1.split('.'))
    v2 = map(int, v2.split('.'))
    for v in (v1, v2):
        while v and v[-1] == 0:
            v.pop()
    return cmp(v1, v2)

def compareVersion2(A, B):
    Alist = map(int, A.split('.'))
    Blist = map(int, B.split('.'))
    if Alist[-1] == 0:
        Alist = Alist[:-1]
    if Blist[-1] == 0:
        Blist = Blist[:-1]
    for i in xrange(min(len(Alist), len(Blist))):
        if Alist[i] > Blist[i]:
            return 1
        elif Alist[i] < Blist[i]:
            return -1
    if len(Alist) == len(Blist):
        return 0
    return -1


A = "7611096.45.537.4"
B = "6.1905074"
print compareVersion(A, B)
