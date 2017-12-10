# Recursive Approach
# No efficient

def search(x, y, path):
    if grid[x][y] == 2:
        return True
    elif grid[x][y] == 1:
        return False
    # already visited
    elif grid[x][y] == 3:
        return False
    # mark as visited
    path.append((x,y))
    grid[x][y] = 3
    # explore neighbors  
    if ((x < len(grid)-1 and search(x+1, y, path))
        or (y > 0 and search(x, y-1, path))
        or (x > 0 and search(x-1, y, path))
        or (y < len(grid)-1 and search(x, y+1, path))):
        return True
    return False


mapp =  grid = [[0, 0, 0, 0, 0, 1],\
                [1, 1, 0, 0, 0, 1],\
                [0, 0, 0, 1, 0, 0],\
                [0, 1, 1, 0, 0, 1],\
                [0, 1, 0, 0, 1, 0],\
                [0, 1, 0, 0, 0, 0]]

start = (0, 0)
target = (5,5)
# mark the target
grid[target[0]][target[1]] = 2
path = []
print search(start[0], start[1], path)
print path
