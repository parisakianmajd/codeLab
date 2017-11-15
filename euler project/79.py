# Passcode derivation
# https://projecteuler.net/problem=79

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) #dictionary of graph adjacency List
        self.V = set()

    def addEdge(self,u,v):
         self.graph[u].append(v)
 
    # A recursive function
    def topologicalSortUtil(self,v,visited,stack):
         visited.add(v)
         for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
         stack.insert(0,v)
 
    def topologicalSort(self):
        visited = set()
        stack =[]
        for n in xrange(len(self.V)):
            if n not in visited:
                self.topologicalSortUtil(n,visited,stack)
        return stack
                

f = open("p079_keylog.txt")
attempts = f.readlines()
graph = Graph()
for line in attempts:
    line = line.strip()
    for i in xrange(len(line) - 1):
        a, b = int(line[i]), int(line[i + 1])
        graph.addEdge(a,b)
        graph.V.add(a)
        graph.V.add(b)
print graph.topologicalSort()
        







    
