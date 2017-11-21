# Given the Inorder and PreOrder traversal of a binary tree, construct the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def buildTree(inOrder, preOrder, start, end):
    if (start > end):
        return None
 
    # select current node from Preorder traversal using
    # preIndex and increment preIndex
    node = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
 
    # If this node has no children then return
    if start == end :
        return node
 
    # find the index of this node in Inorder traversal
    inIndex = search(inOrder, start, end, node.data)
     
    # Using index in Inorder Traversal, construct left 
    # and right subtrees
    node.left = buildTree(inOrder, preOrder, start, inIndex-1)
    node.right = buildTree(inOrder, preOrder, inIndex+1, end)
 
    return node
 
# UTILITY FUNCTIONS
# Function to find index of vaue in arr[start...end]
# The function assumes that value is rpesent in inOrder[]
 
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i
 
def printInorder(node):
    if node is None:
        return
     
    # left child
    printInorder(node.left)
    printInorder(node.right)

    print node.data,
    # right child
     
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.preIndex = 0

root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
 
print "Postorder traversal:"
printInorder(root)
