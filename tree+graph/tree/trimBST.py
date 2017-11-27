# Given a min and a max number, trim the BST such that
# all the numbersare between min and max (inclusive)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def trimBST(root, minVal, maxVal):
    if not root:
        return
    root.left=trimBST(root.left, minVal, maxVal)
    root.right=trimBST(root.right, minVal, maxVal)
    if minVal<=root.val<=maxVal:
        return root
    if root.val<minVal:
        return root.right
    if root.val>maxVal:
        return root.left

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
        
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
printInorder(root)
print
root = trimBST(root,1, 3)
printInorder(root)
