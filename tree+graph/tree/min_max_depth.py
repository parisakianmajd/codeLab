# Given a binary tree, find its max depth.

def maxDepth(self, root):
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Given a binary tree, find its minimum depth.

def minDepth(self, A):
    if A is None:
        return 0
    if A.left is None and A.right is None:
        return  1
    if A.left is None:
        return minDepth(A.right)+1
    if A.right is None:
        return minDepth(A.left)+1
    
    return min(minDepth(A.left), minDepth(A.right))+ 1

def minDepth(self, root):
# do Level Order Traversal
# returns depth of the first leaf
    if root is None:
        return 0 
    q = []
    q.append(root)

    while len(q)>0:
        node = q.pop(0)
        # leaf node
        if node.left is None and node.right is None:    
            return depth 
        
        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append(node.left)

        if node.right is not None:  
            q.append(node.right)
