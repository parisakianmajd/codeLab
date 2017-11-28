#Given a binary tree check if it's a mirror of itself
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root

    def is_side_symmetric(self, n1, n2):
        if n1 == n2:
            return True
        if n1 == None or n2 == None:
            return False
        return n1.val == n2.val and\
               self.is_side_symmetric(n1.left, n2.right)and\
               self.is_side_symmetric(n1.right, n2.left)
    
    def is_symmetric(self, root):
        if root is None:
            return True
        return self.is_side_symmetric(root.left, root.right)
        
