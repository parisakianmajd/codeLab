# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.

# The first call to next() will return the smallest number in BST.
# Calling next() again will return the next smallest number in the BST, and so on.



class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack)!=0
    
    # @return an integer, the next smallest number
    def next(self):
        tmp = self.stack.pop()
        self.pushLeft(tmp.right)
        return tmp.val
        
    def pushLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

class BSTIterator2:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.head = root
        self.ans = []
        temp = self.head
        self.i = 0
        s = []
        while temp or s:
            if temp:
                s.append(temp)
                temp = temp.left
            else:
                temp = s.pop()
                self.ans.append(temp.val)
                temp = temp.right
        self.length = len(self.ans)
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.i < self.length

    # @return an integer, the next smallest number
    def next(self):
        self.i += 1
        return self.ans[self.i-1]
