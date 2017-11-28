#You are in an infinite 2D grid where you can move in any of the 8 directions
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it.

def coverPoints(points):
    steps = 0
    for i in xrange(len(points) - 1):
        x = abs(points[i+1][0] - points[i][0])
        y = abs(points[i+1][1] - points[i][1])
        steps += max(x,y)
    return steps

arr =  [(0, 0), (1, 1), (1, 2)]
print coverPoints(arr)
