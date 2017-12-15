# Find if Given number is power of 2 or not. 


def power(A):
    x=int(A)
    if x>=2 and (x & (x-1))==0:
        return 1
    else:
        return 0
''

def power2(A):
    A = int(A)
    if A == 0 or A == 1:
        return 0
    while A != 1:
        if A % 2 != 0:
            return 0
        A /= 2
    return 1


def power3(A):
    if int(A[-1]) % 2:
        return 0

    binary = bin(int(A))

    for b in binary[1:]:
        if b != '0':
            return 0
    return 1


print power(256)
