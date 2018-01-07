# Given a binary tree, invert the binary tree and return it. 

# Example: 
#
#     1
#   /   \
#  2     3
# / \   / \
#4   5 6   7
# return
#
#     1
#   /   \
#  3     2
# / \   / \
#7   6 5   4
 
def invertTree(root):
    if root is not None:
        nodes = []
        nodes.append(root)
        while len(nodes) > 0:
            node = nodes.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)
    
    return root

def invertTree_recur(root):
    if root is None:
        return
    root.left, root.right = invertTree_recur(root.right), invertTree_recur(root.left)
    return root
