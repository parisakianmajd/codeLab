#For Given Number N find if its COLORFUL number or not

def isColorful(num):
    digits = []
    products = set()
    for d in str(num):
        if d == '1' or d =='0':
            return False
        if num < 10:
            return True
        digits.append(int(d))
        products.add(int(d))
    if len(digits) != len(products):
        return False
    for l in xrange(2,len(digits)):
        for i in xrange(len(digits) - l +1):
            prod = reduce(lambda x,y: x * y, digits[i:i+l])
            if prod in products:
                return False
            products.add(prod)
    return True
        

print isColorful(3562)
print isColorful(3462)
