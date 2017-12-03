# check if a graph is bipartite using bfs
# assign RED to source
# assign BLUE to neigbors
# if any of negibors have the same color as this node, return False

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in xrange(V)] for row in xrange(V)]

    def isBipartite(self, src):
        colorArr = [-1] * self.V
        colorArr[src] = 1

        queue = [src]

        while queue:
            u = queue.pop()
            # if there is a self loop, return False
            if self.graph[u][u] == 1:
                return False
            for v in xrange(self.V):
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    colorArr[v] = 1- colorArr[u]
                    queue.append(v)

                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        return True

graph = Graph(4)
graph.graph= [[0, 1, 0, 1],\
            [1, 0, 1, 0],\
            [0, 1, 0, 1],\
            [1, 0, 1, 0]]
print graph.isBipartite(0)
        
