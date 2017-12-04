#Given a square chessboard of N x N size, the position of Knight and position of a target is given.
# We need to find out minimum steps a Knight will take to reach the target position.

# This problem can be viewed as problem of finding shortest path in unweighted graph
# use BFS
# Time complexity O(n**2)

class Cell:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

def isInside(x, y, n):
    if x >= 1 and x <= n and y >= 1 and y <= n:
        return True
    return False

def minStepToReachTarget(start, target, n):
    # directions that one can move
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    queue = []
    queue.append(Cell(start[0], start[1], 0))
    visited = [[False for i in xrange(n+1)] for j in xrange(n+1)]
    while queue:
        t = queue.pop(0)
        visited[t.x][t.y] = True
        if t.x == target[0] and t.y == target[1]:
            return t.dis
        for i in xrange(len(dx)):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if isInside(x, y, n) and not visited[x][y]:
                queue.append(Cell(x, y, t.dis + 1))

n = 6
start = (4, 5)
end = (1, 1)
print minStepToReachTarget(start, end, n)
 
