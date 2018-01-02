# Implement pow(x, n) % d.


def pow(x, n, d):
    if n == 0:
        return 1%d
    temp = pow(x, n/2, d)
    return (temp*temp)%d if n%2==0 else (x*temp*temp)%d

def pow(x, n, d):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    number = 1
    while n:
        if n & 1:
            number = number * x % d
        n >>= 1
        x = x * x % d
    return number
