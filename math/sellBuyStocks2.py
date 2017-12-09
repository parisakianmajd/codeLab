
 # "devide and conquer". We use left[i] to track the maximum profit for transactions before i,
 #and use right[i] to track the maximum profit for transactions after i. 

def maxProfit(prices):
        n = len(prices)
        if n < 2:
                return 0
        left = [0 for i in xrange(n)]
        right = [0 for i in xrange(n)]

        left[0] = 0

        minBuyPrice = prices[0]
        # DP from left to right
        for i in xrange(1,n):
                minBuyPrice = min(minBuyPrice, prices[i])
                left[i] = max(left[i-1], prices[i] - minBuyPrice)
        # DP from right to left
        right[-1] = 0
        maxSellPrice = prices[-1]

        for i in xrange(n-2, -1, -1):
                 maxSellPrice = max(maxSellPrice, prices[i])
                 right[i] = max(right[i + 1], maxSellPrice - prices[i])

        profit = 0
        for i in xrange(n):
                profit = max(profit, left[i] + right[i])

        return profit

prices = [100, 180, 260, 310, 40, 535, 695]

print maxProfit(prices)
