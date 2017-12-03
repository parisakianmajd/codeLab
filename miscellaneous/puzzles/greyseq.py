#Generate n-bit Gray Codes
#Given a number n, generate bit patterns from 0 to 2^n-1 such
#that successive patterns differ by one bit.

def greySeq(n):
    if n <= 0:
        return
    result = [0,1]
    for i in xrange(1,n):
        for x in range(len(result)-1,-1,-1):
            result += [2**i + result[x]]
    return result



def greySeq2(n):
    if n <= 0:
        return
    result = ['0','1']
    i = 2
    while i < 1<<n:
        for j in xrange(i-1,-1,-1):
            result.append(result[j])
        for j in xrange(i):
            result[j] = '0' + result[j]
        for j in xrange(i, 2**i):
            result[j] = '1' + result[j]
        i = i<<1
    out = []
    for r in result:
        out.append(int(''.join(r),2))
    return out
        



def isGrayCode(num1, num2):
    differences = 0
    while (num1 > 0 or num2 > 0):
        if ((num1 & 1) != (num2 & 1)):
            differences += 1
        num1 >>= 1
        num2 >>= 1
    return differences == 1





print greySeq2(2)
print isGrayCode(0, 3)
print isGrayCode(0, 1)
