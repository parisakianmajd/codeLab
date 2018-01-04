#There are N children standing in a line. Each child is assigned a rating value.

#You are giving candies to these children subjected to the following requirements:
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.


def candy(ratings):
    n = len(ratings)
    if n < 2:
        return n 
    candies = [1] * n 
    for i in xrange(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
    return sum(candies)

A = [1, 2]
print candy(A)
