# Recursive Function
def optCost(i,j,freq):
    if j < i: return 0
    if j == i: return freq[i]
    return sum(freq[i:j+1]) + min([optCost(i, r-1,freq) + optCost(r+1, j,freq) \
                for r in xrange(i, j+1)])


def optimalBST_recursive(freq):
    n = len(freq)
    return optCost(0, n-1,freq)

# Dynamic Programming Approach
def optimalBST(freq):
    n = len(freq)
    cost = [[0 for x in range(n+1)] for x in range(n+1)]
    
    for i in range(n):
        cost[i][i] = freq[i]
 
    # L is chain length.
    for L in range(2, n+1):
        for i in range(n-L+2):
            j = i+L-1
            cost[i][j] = min([((cost[i][r-1] if r > i else 0) + \
                    (cost[r+1][j] if r < j else 0) +\
                    sum(freq[i:j+1])) for r in xrange(i, j+1)])
    return cost[0][n-1]


freq = [34, 8, 50]
n = len(freq)

print optimalBST_recursive(freq)
print optimalBST(freq)
