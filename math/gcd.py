def gcd(a, b):
    if a < b: return gcd(b,a)
    '''Return greatest common divisor using Euclid's Algorithm.'''
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    '''Return lowest common multiple.'''
    return a * b // gcd(a, b)

def lcmm(arr):
    '''Return lcm of args'''   
    return reduce(lcm, arr)
