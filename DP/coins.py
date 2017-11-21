coins = [1,2,3]
total = 4

m = len(coins)
table = [[0 for i in xrange(total+1)] for j in xrange(m)]

for i in xrange(total+1):
    table[0][i] = i
    
for i in xrange(1,m):
    for j in xrange(1,total+1):
        if j < coins[i]:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = min(table[i-1][j], table[i][j-coins[i]] + 1)

for t in table:
    print t

print table[m-1][total]

table = [[0 for i in xrange(total+1)] for j in xrange(m)]

for i in xrange(m):
    table[i][0] = 1
    
for i in xrange(1,m):
    for j in xrange(1,total+1):
        if j < coins[i]:
            table[i][j] = 1
        else:
            x = table[i-1][j]
            y = table[i][j-coins[i]]
            table[i][j] = x + y


for t in table:
    print t

print table[m-1][total]
