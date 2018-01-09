# convert a sorted array to a height balanced BST

def arrayToBST(arr, start, end):
    # Get the middle element and set it as the root
    # do a recursive call of left and right children
    if  start > end:
        return None
    mid = (start + end) / 2
    root = TreeNode(arr[mid])
    root.left = arrayToBST(arr, start, mid - 1)
    root.right = arrayToBST(arr, mid + 1, end)
    return root

def sortedArrayToBST(arr):
    return arrayToBST(arr, 0, len(A) - 1)
