# Given a graph and a source vertex in graph, find shortest paths from source to all vertices in the given graph.
# Dijikstra algorithm generates a SPT (shortest path tree)

# Keep two sets of vertices included in the path and those not included (other)
# at each step find a vertex in the other set with minimum distance from source
# adapted from: http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/


import sys
 
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in xrange(vertices)] 
                      for row in xrange(vertices)]
 
    def printSolution(self, dist):
        print "Vertet \t Distance from Source"
        for node in range(self.V):
            print node,"\t",dist[node]
 
    # Find the vertex with minimum distance from the others set
    def minDistance(self, dist, selected):
 
        minDist = sys.maxint
        for v in xrange(self.V):
            if dist[v] < minDist and selected[v] == False:
                minDist = dist[v]
                minIndex = v
 
        return minIndex
 
    def dijkstra(self, src):
 
        dist = [sys.maxint] * self.V
        dist[src] = 0
        selected = [False] * self.V
 
        for v in range(self.V):
            u = self.minDistance(dist, selected)
            selected[u] = True
 
            # Update dist value of the adjacent vertices of the picked vertex
            # if the new distance is shortted and the vertex is not included in the path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and selected[v] == False and \
                   dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
g  = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],\
           [4, 0, 8, 0, 0, 0, 0, 11, 0],\
           [0, 8, 0, 7, 0, 4, 0, 0, 2],\
           [0, 0, 7, 0, 9, 14, 0, 0, 0],\
           [0, 0, 0, 9, 0, 10, 0, 0, 0],\
           [0, 0, 4, 14, 10, 0, 2, 0, 0],\
           [0, 0, 0, 0, 0, 2, 0, 1, 6],\
           [8, 11, 0, 0, 0, 0, 1, 0, 7],\
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
 
g.dijkstra(0)
 
