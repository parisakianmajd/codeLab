# Find the prime number which can be written as the sum of the most consecutive primes smaller than or equal to limit.

from collections import defaultdict

def primes_sieve(limit):
    sieve = [True] * limit                          
    sieve[0] = sieve[1] = False

    for (i, isprime) in enumerate(sieve):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     
                sieve[n] = False



def longest_consecutive_prime_sum(until):
    primes = []
    sieve = primes_sieve(until)
    for s in sieve:
        if s:
            primes.append(s)

    primes_set = set(primes)
    primes_sum = [0]
    
    # find the pefix array (primes_sum)
    # the prefix array helps to find the sum of subsets fast then for each subset we check if the sum is prime
    # if so this can be a candide answer, but we'll continue searching until the sum is greater than the limit
    
    for i in range(0, len(primes)):
        primes_sum.append(primes_sum[i] + primes[i])
    total_primes = 0
    result = 0
    for i in range(0, len(primes_sum)):
        for j in range(i - (total_primes + 1), -1, -1):
              if primes_sum[i] - primes_sum[j] > until:
                break

              if primes_sum[i] - primes_sum[j] in primes_set:
                total_primes = i - j
                result = primes_sum[i] - primes_sum[j]

    return result


print longest_consecutive_prime_sum(100)

