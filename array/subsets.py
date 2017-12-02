# return all subsets
from itertools import combinations
def subsets(S):
    if len(S) == 0:
        return [[]]

    x = subsets(S[1:])

    return x + [[S[0]] + y for y in x]


def subsets2(S):
    result = [[]]
    for x in S:
        result.extend([subset + [x] for subset in result])
    return sorted(result)
# print subsets in lexicographically sorted order
def subsets3(S):
    S = sorted(S)
    subsets = []
    for i in xrange(len(S) + 1):
        subsets.extend(set(combinations(S, i)))
    return subsets
# e.g. Set  = [a,b,c]
# power_set_size = 2 ** 3 = 8
# Run for binary counter = 000 to 111
# left shift x << n == x * 2**n
def subsets4(S):
    n = len(S)
    powersetSize = 2 ** n
    subsets = set()
    S.sort()
    for counter in xrange(powersetSize):
        subset = []
        for j in xrange(n):
          #Check if jth bit in the counter is set
           #If set then print jth element from set
          if counter & (1<<j):
              subset.append(S[j])
        subsets.add(tuple(subset))
    return map(list, sorted(subsets))


S = [1,2,2]
print subsets2(S)
print subsets3(S)
print subsets4(S)


