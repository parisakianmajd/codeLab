# implementing dfs using stack 
# and bfs using queue

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    return path

def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex not in path:
            path.append(vertex)
        for neighbor in graph[vertex][::-1]:
            stack.append(neighbor)
    return path

def bfs_recursive(graph, queue, path=[]):
    if len(queue) == 0:
        return path
    w = queue.pop(0)
    if w not in path:
        path.append(w)
    for neighbor in graph[w]:
        queue.append(neighbor)
    return bfs_recursive(graph, queue, path)

        
def bfs(graph, start):
    visited = {}
    for w in graph:
        visited[w] = False
    path, queue = [],[start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        path.append(vertex)
        for w in graph[vertex]:
            if visited[w] == False:
                queue.append(w)
                visited[w] = True
    return path

graph = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}
print dfs_recursive(graph, 1)
print dfs_iterative(graph, 1)
print bfs(graph, 1)
print bfs_recursive(graph, [1])
