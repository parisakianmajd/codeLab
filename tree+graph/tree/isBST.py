# Given a Binary tree check if it's BST
import sys

class Node:
    def __init__(self, val):
        self.left, self.right, self.val = None, None, val

def isBST(root, minVal = -sys.maxint, maxVal = sys.maxint):
    if root is None:
        return True
    
    if not minVal < root.val < maxVal:
        return False
    
    return isBST(root.left, minVal, root.val) and \
           isBST(root.right, root.val, maxVal)

#using Null pointers
def isBST2(root, left = None, right = None):
    if root is None:
        return True

    if left is not None and root.val < left.val:
        return False
    if right is not None and root.val > right.val:
        return False

    return isBST2(root.left, left, root) and\
           isBST2(root.right, root, right)


# if tree is BST, the tree's inorder traversal gives a sorted arr

# Default values are initialized only when the function is first evaluated,
# not each time it is executed, so you can use a list or any other mutable object to store static values.

def isBST3(root, prev = [-sys.maxint]):
    if root is None:
        return True
    
    if not isBST3(root.left, prev):
        return False

    if root.val <= prev[0]:
        return False
    
    prev[0] = root.val

    return isBST3(root.right, prev)

def isBST4(**kwargs):
    def decorate(isBST4_new):
        for k in kwargs:
            setattr(isBST4_new, k, kwargs[k])
        return isBST4_new
    return decorate
    
@isBST4(prev = None)
def isBST3_new(root):

    if root:
        if not isBST3_new(root.left):
            return False
        
        if isBST3_new.prev != None and root.val <= isBST3_new.prev.val:
            return False
        
        isBST3_new.prev = root
        return isBST3_new(root.right)
    return True
 


    
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(5)
print isBST(root)
print isBST2(root)
print isBST3(root)
#isBST3_new.prev = None
print isBST3_new(root)

