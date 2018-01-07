# Given an inorder traversal of a cartesian tree, construct the tree.
# Cartesian tree is a heap ordered binary tree, where the root is greater than all the elements in the 
# No duplicates exist in the tree

def buildTree(inorder):
# similar to construction of tree from given Inorder and Preorder traversals
# the maximum element in given array must be root.

    if len(inorder) == 0 :
        return None
    maxVal = max(inorder)
    i = inorder.index(maxVal)
    root = TreeNode(maxVal)
    root.left = self.buildTree(inorder[:i])
    root.right = self.buildTree(inorder[i+1:])
    return root
