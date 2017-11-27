from itertools import permutations
# Generate all permutations of a string

def findPermutations(inStr):
    if len(inStr) <= 1:
        return [inStr]
    perms = findPermutations(inStr[1:])
    char = inStr[0]
    result = []
    for p in perms:
        for i in xrange(len(p) + 1):
            result.append(p[:i] + char + p[i:])
    return result

# Generator
def findPermutations2(inStr):
    if len(inStr) <= 1:
        yield inStr
    perms = findPermutations(inStr[1:])
    char = inStr[0]
    for p in perms:
        for i in xrange(len(p) + 1):
            yield p[:i] + char + p[i:]


inStr = 'abcde'

print [''.join(p) for p in permutations(inStr)]
print findPermutations(inStr)
print [''.join(p) for p in findPermutations2(inStr)]
