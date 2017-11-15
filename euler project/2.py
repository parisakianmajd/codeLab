from itertools import permutations
from math import sqrt


def circularPrime(n, primes):
    for p in permutations(str(n)):
        #if not isPrime(int(''.join(p))):
        #    return False
        if int(''.join(p)) not in primes:
            return False
    return True

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for x in range(4,n+1,2):
        primes[x] = False

    for x in range(3,int(sqrt(n))+1,2):
        if(primes[x]):
            for y in range(x*x,n+1,x):
                primes[y] = False

    return primes
def rotate(n):
    n=str(n)
    return n[1:]+n[:1]


def isRotatable(n, primes):
    for x in range(2,n):
        n = rotate(n)
        if int(n) not in primes:
            return False
    return True


n= 1000000
sievePrime = sieve(n)
primes = []
for index, s in enumerate(sievePrime):
    if s == True:
        primes.append(index)    
circs = []
for x in range(2, len(primes)):
    print x
    if(isRotatable(x,primes)):
        circs.append(x)
print circs
print len(circs)
