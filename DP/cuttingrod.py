# Given a rod of length n and
# an array of prices for all pieces smaller than n.
# Find the maximum value obtainable by cutting up the rod and selling the pieces

def cuttingRod(L, lengths, prices, n):
    table = [[0 for x in range(L+1)] for x in range(n)]

    for i in xrange(1,L+1):
        table[0][i] = (i/lengths[0]) * prices[0]

    for i in range(1,n):
        for l in range(1,L+1):
            if l >= i+1:
                table[i][l] = max(table[i-1][l], prices[i] + table[i][l-i-1])
            else:
                table[i][l] = table[i-1][l]
    for t in table:
        print t
    return table[n-1][L]

 
prices = [2,5,7,8]
lengths = [1, 2, 3, 4]
L = 5
n = len(prices)
print cuttingRod(L, lengths, prices, n)
L = 8
prices2= [1, 5, 8, 9, 10, 17, 17, 20]
lengths2 = [1, 2, 3, 4, 5, 6, 7, 8]
print cuttingRod(L, lengths2, prices2, len(lengths2))
