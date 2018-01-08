#  There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.

# Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.

def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    res = 0
    current = 0
    for i in xrange(len(gas)):
        current += gas[i] - cost[i]
        if current < 0:
            current = 0
            res = i + 1
    return res
