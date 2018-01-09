# Given a binary tree and a sum,
# Find all root-to-leaf paths where each path's sum equals the given sum.

def pathSum(root, target):
    res = []
    
    def helper(root, target, path):
        if not root:
            return 
        if  not root.left and not root.right:
            if target == root.val:
                res.append(path + [root.val])
            return
        helper(root.left , target-root.val , path + [root.val])
        helper(root.right , target-root.val , path + [root.val])
    
    helper(root, target, [])
    return res

# 2nd version -- sloppy - recursive
def pathSum(self, A, B):
    return self.traverse(A, B, [], [])

def traverse(self, root, B, path, paths):
    path = path[:]
    path.append(str(root.val))
    if root.left is None and root.right is None:
        #if it's a leaf
        if sum(map(int,path)) == B:
            paths.append(path)
    else: 
        if root.left:
            traverse(root.left, B, path, paths)
        if root.right:
            traverse(root.right, B, path, paths)
    return paths
