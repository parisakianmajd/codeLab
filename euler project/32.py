def is_pandigital(n):
    n = str(n)
    return len(n)== 9 and not '123456789'.strip(n)

p = set()
for i in range(2,  100):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print "Sum of products =", sum(p)
