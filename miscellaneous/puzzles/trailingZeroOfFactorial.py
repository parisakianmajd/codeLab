from math import factorial

#Given an integer n, return the number of trailing zeroes in n!

# every multiple of 5 there are at least 2 even numbers so we just need to count the numbre of 5s
def trailingZeroes_recur(n):
    if n < 5:
        return 0
    return trailingZeroes(n/5) + n/5

def trailingZeroes(n):
    if n < 5:
        return 0
    i = 1
    count = 0
    while n/i >= 1:
        i *= 5
        count += n/i
    return count


print trailingZeroes(1000)

# bruth force
f = str(factorial(1000))
zeros = 0
while f[-1] == '0':
    f = f[:-1]
    zeros += 1
print zeros
