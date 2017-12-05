#Find the min number of steps to reach the destination in snake, ladder game

#Every vertex of the graph has an edge to next six vertices if next 6 vertices do not have a snake or ladder.
#If any of the next six vertices has a snake or ladder,
# then the edge from current vertex goes to the top of the ladder or tail of the snake

# use BFS
# N =  number of cells in the given board
# move[0...N-1]; entry move[i] is -1 if there is no snake and no ladder from i
# otherwise move[i] contains index of destination cell for the snake or the ladder at i

class Cell:
    def __init__(self, v, dist):
        self.v = v # vertext
        self.dist = dist  # distance from the source


def getMinDiceThrows(move, n):
    visited = [False for i in xrange(n)]

    queue = []

    visited[0] = True
    start = Cell(0,0)
    queue.append(start)

    while queue:
        q = queue.pop(0)
        # if this is the destination cell
        if q.v == n-1:
            break
        # check the 6 neighboring cells
        for j in xrange(q.v+1, q.v+6+1):
            if j < n:
                if not visited[j]:
                    dist = q.dist + 1
                    visited[j] = True
                if move[j] != -1:
                    a = move[j]
                else:
                    a = j
                queue.append(Cell(a, dist))
    return q.dist
 
N = 30
moves = [-1 for i in xrange(N)]


# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
 
print getMinDiceThrows(moves, N)
