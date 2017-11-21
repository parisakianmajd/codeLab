class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),
 
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)



def bfs(root):
    if root is None:
        return
     
    queue = [root]
 
    while len(queue) > 0:
        # Print front of queue and remove it from queue
        print queue[0].data,
        node = queue.pop(0)
 
        #push left child
        if node.left is not None:
            queue.append(node.left)
 
        # push right child
        if node.right is not None:
            queue.append(node.right)


def iterativeInOrder(current):
    nodeStack = [] 
     
    while True:
        if current is not None:
            nodeStack.append(current)
            current = current.left 
        else:
            if len(nodeStack) > 0:
                current = nodeStack.pop()
                print current.val,
                current = current.right 
            else:
                break
            
def iterativePreOrder(root):
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)
 
    #  Pop all items one by one. Do following for every popped item
    #   a) print it
    #   b) push its right child
    #   c) push its left child

    while len(nodeStack) > 0:
        node = nodeStack.pop()
        print node.val,
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)
            
def iterativePostOrder(root):
    #1. Push root to first stack.
    #2. Loop while first stack is not empty
       #2.1 Pop a node from first stack and push it to second stack
       #2.2 Push left and right children of the popped node to first stack
    #3. Print contents of second stack
    if root is None:
        return         
     
    s1 = []
    s2 = []
     
    s1.append(root)
     
    while len(s1) >0:
         
        # Pop an item from s1 and append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of removed item to s1
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None :
            s1.append(node.right)
 
        # Print all eleements of second stack
    while len(s2) > 0:
        node = s2.pop()
        print node.val,


        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


printPreorder(root)
print ('\n')
iterativePreOrder(root)
print ('\n')
printInorder(root)
print ('\n')
iterativeInOrder(root)
print ('\n')
printPostorder(root)
print ('\n')
iterativePostOrder(root)

