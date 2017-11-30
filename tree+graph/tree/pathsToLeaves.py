# Find all root to leaves paths

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def parse(root, p, paths):
    path = p[:]
    # [:] a shallow copy of the list. a slice from the begining to end that doesn't change the list itself 
    path.append(str(root.val))
    if root.left is None and root.right is None:
        #if it's a leaf
        paths.append(path)
        print('-> '.join(path))
    else: 
        if root.left:
            parse(root.left, path, paths)
        if root.right:
            parse(root.right, path, paths)
    
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
path = []
paths = []
parse(root, path, paths)
print paths
