# Given a binary search tree, write a function to find the kth smallest element in the tree.

# Solution: inorder traversal

def kthsmallest(root, k):
    count = 0
    stack = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                break


def kthsmallest2(root, k):
    inorder = []
    
    def inorderTraverse(root):
        if not root:
            return 
        inorderTraverse(root.left)
        inorder.append(root.val)
        inorderTraverse(root.right)
    
    inorderTraverse(root)
    return inorder[k-1]
