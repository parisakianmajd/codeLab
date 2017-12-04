# Given N and M find all stepping numbers in range N to M
# A number is called as a stepping number if the adjacent digits have a difference of 1.
# e.g 123

# Every node in the graph represents a stepping number;
#there will be a directed edge from a node U to V if V can be transformed from U.
# A Stepping Number V can be transformed from U in following manner.
# U*10 + lastDigit + 1
# U*10 + lastDigit - 1

# Edge Cases: When the last digit of U is 0 or 9
# if the lastDigit is 0, only '1' can be appended.
# if the lastDigit is 9, only '8' can be appended.

def bfs(n, m, digit):
    queue =[digit]
    out = []
    while queue:
        stepNum = queue.pop(0)
        # stepNum = queue.pop()  // if we do dfs
        if stepNum <= m and stepNum >= n:
            out.append(stepNum)
        if stepNum == 0 or stepNum > m:
            continue
        lastDigit = stepNum % 10
        stepNumA = stepNum * 10 + (lastDigit- 1)
        stepNumB = stepNum * 10 + (lastDigit + 1)
        if (lastDigit == 0):
            queue.append(stepNumB)
        elif  (lastDigit == 9):
            queue.append(stepNumA)
        else:
            queue.append(stepNumB)
            queue.append(stepNumA)
    return out


def steppingNums(n, m):
    out = []
    for i in xrange(10):
        out += dfs(n, m, i)
    return sorted(out)


print steppingNums(1, 5800)
