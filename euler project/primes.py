# All prime numbers, other than 2 and 3, are of the form 6n+/-1.
def isPrime(n):
    if n <= 1:
        return False
    if n==2 or n == 3:
        return True
    if n % 2==0 or n %3 == 0:
        return False
    if n < 9:
        return True
    f = 5
    limit = n ** 0.5
    while f <= limit:
        if n % f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True


def sieve(n):
  primes = [True] * (n+1)
  for p in range(2, n+1):
    if (isPrime(p)):
      for i in range(p, n+1, p):
        primes[i] = False
  return primes


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):   
                a[n] = False
def primes_sieve(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    primes = []
    for i in xrange(limit):
        if sieve[i]:
            primes.append(i)
            for n in xrange(i * i, limit, i):
                sieve[n] = False
    return primes
print primes_sieve(100)
    
