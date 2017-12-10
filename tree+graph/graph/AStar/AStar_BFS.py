class Graph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, node):
        return self.edges[node]

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
    
    def in_bounds(self, node):
        (x, y) = node
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, node):
        return self.grid[node[0]][node[1]] == 0
    
    def neighbors(self, v):
        (x, y) = v
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
    
def breadth_first_search(graph, start, goal):
    frontier = [start]
    came_from = {}
    came_from[start] = None
    
    while frontier:
        current = frontier.pop(0)
        if current == goal:
            print "Reached the target!"
            break
        for n in graph.neighbors(current):
            if n not in came_from:
                frontier.append(n)
                came_from[n] = current
    return came_from

mapp =  grid = [[0, 0, 0, 0, 0, 1],\
                [1, 1, 0, 0, 0, 1],\
                [0, 0, 0, 1, 0, 0],\
                [0, 1, 1, 0, 0, 1],\
                [0, 1, 0, 0, 1, 0],\
                [0, 1, 0, 0, 0, 0]]

g = Grid(mapp)
start = (0, 0)
target = (5,5)
parents = breadth_first_search(g,start ,target )
# rebuid the path
node = target
path = []
while node != start:
    path.append(node)
    node = parents[node]
print path[::-1]
    

