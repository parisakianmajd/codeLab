#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#An example is the root-to-leaf path 1->2->3 which represents the number 123.
#Find the total sum of all root-to-leaf numbers % 1003.

class Solution:
    # @param A : root node of tree
    # @return an integer
    def parse(self, root, path, currentValue):
        currentValue += root.val
        if root.left is None and root.right is None:
            path.append(currentValue)
        else: 
            currentValue *= 10
            if not root.right:
                self.parse(root.left, path, currentValue)
            elif not root.left:
                self.parse(root.right, path, currentValue)
            else:
                self.parse(root.right, path, currentValue)
                self.parse(root.left, path, currentValue)
                

    def sumNumbers(self, A):
        path = []
        currentValue = 0
        self.parse(A, path, currentValue)
        return sum(path)  % 1003
