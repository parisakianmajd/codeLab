# Given a binary search tree T, where each node contains a positive integer,
# and an integer K
# Find whether or not there exist two different nodes A and B such that A.value + B.value = K

# Solution
# inorder traversal of the BST gives a sorted array
# use the pointer approach to find if there are two values that sum up to target

def inorder(root):
    stack = []
    current = root
    out = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                out.append(current.val)
                current = current.right
            else:
                break
    return out

def t2Sum(A, B):
    if A is None or B == 0:
        return 0
    arr = inorder(A)
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == B:
            return 1
        elif arr[left] + arr[right] < B:
            left += 1
        else:
            right -=1
    return 0


# 2nd version
# using hashmap

def t2Sum2(root, K):
    def helper(root, K, targets):
        if root is None or K == 0:
            return 0
        if root.val >= K:
            return helper(root.left, K, targets)
        if root.val in targets:
            return 1
        else:
            targets.append[K - root.val] = 1
            return helper(root.left, K, targets) or helper(root.right, K, targets)
    return helper(root, K, {}) 
