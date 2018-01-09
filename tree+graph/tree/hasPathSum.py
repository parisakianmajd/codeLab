# Given a binary tree and a sum,
# determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Solution Approach:
#  do a preorder traversal of the tree. In the preorder traversal,
# keep track of the value calculated till the current node,

def hasPathSum(root, B):
    if root is None:
        return B == 0
    else:
        ans = False
        subSum = B - root.val
         
        # If we reach a leaf node and sum becomes 0, then 
        # return True 
        if subSum == 0 and root.left == None and root.right == None:
            return 1
        if root.left is not None:
            ans = ans or hasPathSum(root.left, subSum)
        if root.right is not None:
            ans = ans or hasPathSum(root.right, subSum)
 
    return ans 
