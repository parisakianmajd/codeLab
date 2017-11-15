#0-1 knapsack Problem

def knapSack(W, wt, val, n):
    table = [[0 for x in range(W+1)] for x in range(n+1)]
 
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1] <= w:
                table[i][w] = max(val[i-1] + table[i-1][w-wt[i-1]], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]
 
    return table[n][W]
 
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W, wt, val, n)
