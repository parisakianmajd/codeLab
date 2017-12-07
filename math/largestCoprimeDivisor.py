# Largest Coprime Divisor
# Given numbers A and B, find the maximum valued integer X such that:

#X divides A i.e
#X and B are co-prime i.e. gcd(X, B) = 1


def gcd(A, B):
    if B > A:
        return self.gcd(B, A)
    while B:
        A, B = B, A%B
    return A
    
def cpFact(A, B):
    p = gcd(A,B)
    while p != 1:
        A /= p
        p = gcd(A,B)
    return A
