#Given a binary tree, return the zigzag level order traversal of its nodes' values.
#(ie,from left to right, then right to left for the next level and alternate between).


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def zigzagLevelOrder2(root):
        res = []
        if root is None:
            return res

        queue = [root]
        leftToRight = True
        while queue:
            res.append(node.val for node in (queue if leftToRight else reversed(queue)))
            queue = [ child for node in queue
                            for child in [node.left, node.right]
                            if child is not None ]
            leftToRight = not leftToRight

        return res
    def zigzagByLayer(zigzagTraverse, currentLayer, leftToRight):
        if len(currentLayer) == 0:
            return
        zigzagTraverseNodes = []
        zigzagTraverseValues = []
        for k in xrange(len(currentLayer)):
            zigzagTraverseNodes.append(currentLayer[k])
            zigzagTraverseValues.append(currentLayer[k].val)
        # append the current row   
        zigzagTraverse.append(zigzagTraverseValues)
        nextLayer = []
        leftToRight = not leftToRight
        while zigzagTraverseNodes:
            node = zigzagTraverseNodes.pop(-1)
            if leftToRight:
                if node.left is not None:
                    nextLayer.append(node.left)
                if node.right is not None:
                    nextLayer.append(node.right)
            else:
                if node.right is not None:
                    nextLayer.append(node.right)
                if node.left is not None:
                    nextLayer.append(node.left)
        zigzagByLayer(zigzagTraverse, nextLayer, leftToRight)
        
    def zigzagLevelOrder(A):
        # do a bfs with two stacks for nodes and the values
        currentLayer = [A]
        zigzagTraverse = []
        zigzagByLayer(zigzagTraverse, currentLayer, True)
        return zigzagTraverse

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


print zigzagLevelOrder(root)
