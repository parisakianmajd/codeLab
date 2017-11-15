
def cancelable(a,b):
    commonDigits = set(str(a)) & set(str(b))
    if commonDigits:
        if a /b == int(str(a).remove(commonDigits)) /int(str(b).remove(commonDigits)):
            return True
    return False
    



fractions = []
for a in xrange(100):
    print a
    for b in xrange(100):
        if cancelable(a,b):
            fractions.append((a,b))

print fractions
