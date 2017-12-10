# Stock Buy Sell to Maximize Profit
#1. Find the local minima and store it as starting index. If not exists, return.
#2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
#3. Update the solution (Increment count of buy sell pairs)
#4. Repeat the above steps if end is not reached.


def stockBuySell(prices):
    n = len(prices)
    if n == 1:
        return
    solutions = []
    i = 0
    while i < n-1:
        while i < n-1 and prices[i+1] <= prices[i]:
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1
        while i < n and prices[i] > prices[i-1]:
            i += 1
        sell = i - 1
        solutions.append((buy, sell))


    return solutions
prices = [1,2,1]
solutions = stockBuySell(prices)
profit = 0
for s in solutions:
    print "Buy on : %d,  Sell on day: %d" % (s[0], s[1])
    profit += prices[s[1]] - prices[s[0]]
print profit
