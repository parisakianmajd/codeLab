#Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.


def getColums(grid):
    # * .. unpacking 
    return zip(*grid)

def getRows(grid):
    return [[c for c in r] for r in grid]

def anti_diagonal(grid):
    b = [None] * (len(grid) - 1)
    newGrid = []
    for i,r in enumerate(getRows(grid)):
        newGrid.append(b[:i] + r + b[i:])
    return [[c for c in r if c is not None] for r in getColums(newGrid)]
        

grid = [[1, 2, 3], \
        [4, 5, 6],\
        [7, 8, 9]]

print anti_diagonal(grid)
