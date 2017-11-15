d = ''.join(map(str, range(1000000)))
digits = 1
for i in xrange(6):
    digits *= int(d[10**i])
print digits


    
