def is_pandigital(n):
    n = str(n)
    return len(n)== 9 and not '123456789'.strip(n)

def is_pandigital_multiple(n):
    digits = set(str(n))
    i = 2
    pand = str(n)
    while len(digits) < 9:
        digit =str(n*i)
        new_digits = set(digit)
        for nd in new_digits:
            if nd == '0':
                return False
            if nd in digits:
                return False
            digits.add(nd)
        pand += digit
    if len(digits) == 9:
        return pand

maxNum = 0
p = set()
for i in range(10000):
    pand = is_pandigital_multiple(i)
    if pand and pand > maxNum:
        maxNum = pand

print maxNum
