import heapq
import sys

def maxp3(A):
    if len(A) < 3:
        return 0
    max3 = heapq.nlargest(3,A)
    neg = filter(lambda x: x < 0, A)
    max_neg = heapq.nsmallest(2, neg)
    max_neg.append(max3[0])
    posp = reduce(lambda x,y: x*y,max3)
    negp = reduce(lambda x,y: x*y,max_neg)
    return max(posp, negp)


def maxp3_2(A):
    l = len(A)
    if l == 3:
        return A[0]*A[1]*A[2]
    m1 = -sys.maxint
    m2 = -sys.maxint
    m3 = -sys.maxint
    for a in A:
        if a > m1:
            m3 = m2
            m2 = m1
            m1 = a
        elif a > m2:
            m3 = m2
            m2 = a
        elif a > m3:
            m3 = a
    neg = [abs(a) for a in A if a<0]
    if len(neg)<2:
        return m1 * m2 * m3
    n1 = 0
    n2 = 0
    for a in neg:
            if a <= n2:
                continue
            elif n2 < a <= n1:
                n2 = a
            else:
                n2 = n1
                n1 = a 
    return max(m1*m2*m3, m1*n1*n2)


A = [0, -1, 3, 100, 70, 50]
A = [ 0, -1, 3, 100, -70, -50 ]

print maxp3(A)
print maxp3_2(A)
