# Find the lowest common ancestor in a BST

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 

def findLCA(root, n1, n2):
    if root.key > max(n1, n2):
        return findLCA(root.left, n1, n2)
    elif root.key < min(n1, n2):
        return findLCA(root.right, n1, n2)
    return root.key


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(14)
    root.left.left = Node(5)
    root.left.right = Node(9)
    root.right.left = Node(11)
    root.right.right = Node(12)
     
    print "LCA(11, 12) = %d" %(findLCA(root, 11, 12))
    print "LCA(11, 5) = %d" %(findLCA(root, 11, 5))
    print "LCA(9, 5) = %d" %(findLCA(root, 9, 5))

