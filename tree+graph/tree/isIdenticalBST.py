# Given two binary trees, write a function to check if they are equal or not.

def isSameTree(A, B):
    if A is None and B is None:
        return True
    elif A is None or B is None:
        return False
    return A.val == B.val and self.isSameTree(A.left, B.left) and\
    self.isSameTree(A.right, B.right):
