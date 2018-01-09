# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.

def traverse(root, val):
    if root is None:
        return 0
    value = value * 10 + root.val
    
    if root.left is None and root.right is None:
        return value
    
    return traverse(root.left, value) + traverse(root.right,value)
    
def sumNumbers(root):
    return traverse(root, 0) % 1003
