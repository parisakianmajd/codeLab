# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n

def matrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = min([m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] for k in range(i,j)])
    return m[1][n-1]


 
arr = [1, 2, 3 ,4]
size = len(arr)
 
print matrixChainOrder(arr, size)
