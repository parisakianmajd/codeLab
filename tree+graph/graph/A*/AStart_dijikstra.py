import heapq

class priority_queue:
    def __init__(self):
        self._queue = []
        # index is used to sort the items in order they were inserted
        self._index = 0

    def put(self, item, priority):
        #heappq implements a min heap, i.e. heappop return the smallest item 
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    def size(self):
        return len(self._queue)
    def get(self):
        # get the next task
        return heapq.heappop(self._queue)[-1]
        
class GridWithWeights:
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)
    
    def in_bounds(self, node):
        (x, y) = node
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, node):
        return (node[0], node[1]) not in self.walls
    
    def neighbors(self, v):
        (x, y) = v
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
    
def dijkstra_search(graph, start, target):
    pq = priority_queue()
    pq.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while pq.size()!=0:
        current = pq.get()
        
        if current == target:
            break
        
        for n in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost
                pq.put(n, priority)
                came_from[n] = current
    
    return came_from, cost_so_far




g = GridWithWeights(10, 10)
g.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
g.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),\
                                   (4, 3), (4, 4), (4, 5), (4, 6),\
                                   (4, 7), (4, 8), (5, 1), (5, 2),\
                                   (5, 3), (5, 4), (5, 5), (5, 6), \
                                   (5, 7), (5, 8), (6, 2), (6, 3), \
                                   (6, 4), (6, 5), (6, 6), (6, 7), \
                                   (7, 3), (7, 4), (7, 5)]}
start = (0, 0)
target = (9,9)
parents, cost =  dijkstra_search(g,start ,target)

# rebuid the path
node = target
path = []
totalCost = 0
while node != start:
    path.append(node)
    node = parents[node]
    totalCost += cost[node]
print "Total Cost:" + str(totalCost)
print path[::-1]


