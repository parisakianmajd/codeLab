#Given preorder and inorder traversal of a tree, construct the binary tree.


def buildTree(preorder, inorder):
    
    head = None
    
    def helper( head, preorder, inorder ):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        head = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        length = len(inorder[:index])
        head.left = helper(head, preorder[1:1+length], inorder[:index])
        head.right = helper(head, preorder[1+length:], inorder[index+1:])
        return head
    
    head = helper(head, preorder , inorder)
    return head
