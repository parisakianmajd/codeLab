#Given inorder and postorder traversal of a tree, construct the binary tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    head = None
    
    def helper(head , inorder , postorder ):
        if len(inorder) == 0:
            return None
        head = TreeNode(postorder[-1])
        index = inorder.index(head.val)
        length = len(inorder[:index])
        head.left = helper(head, inorder[:index], postorder[:length])
        head.right = helper(head, inorder[index+1:], postorder[length:-1])
        return head
    
    head = helper(head, inorder, postorder)
    return head
