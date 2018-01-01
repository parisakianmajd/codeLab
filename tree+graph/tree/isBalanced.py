# Given a binary tree, determine if it is height-balanced.


def isBalanced(root):
    return isBalancedInt(root) >= 0:
    
def isBalancedInt(self, root):
    if root == None:
        return 0
        
    left = isBalancedInt(root.left)
    right = isBalancedInt(root.right)
    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max(left, right) + 1



def no_kids(root):
    return not root.left and not root.right

def isBalanced2(root):
    if ((not root.left) and ((not root.right) or no_kids(root.right))) or \
    ((not root.right) and ((not root.left) or no_kids(root.left))):
        return True
    elif ((not root.left) and (root.right.left or root.right.right)) or \
    ((not root.right) and (root.left.left or root.left.right)):
        return False
    return isBalanced2(root.left) and isBalanced2(root.right):
