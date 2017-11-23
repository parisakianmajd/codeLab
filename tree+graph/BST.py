class Node():
    def __init__(self, data, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


def search(root, value):
    if root is None or root.data == value:
        return root
    
    current = root
    while current.data != value:
        if current.data > value:
            if current.leftChild != None:
                current = current.leftChild
            else:
                return False
        else:
            if current.leftChild != None:
                current = current.rightChild
            else:
                return False
    return True

def search_recursive(root, value):
    if root is None:
        return False
    if root.data == value:
        return True

    if root.data < value:
        return search_recursive(root.rightChild, value)

    return search_recursive(root.leftChild, value)

def insert(root, value):
    if root is None:
        return Node(value)
    # worst case time O(n)
    # if the tree is a balanced AVL tree, the worst case is O(logn)
    current = root
    while current.data != value:
        if current.data > value:
            if current.leftChild != None:
                current = current.leftChild
            else:
                current.leftChild = Node(value)
                return 
        else:
            if current.rightChild != None:
                current = current.rightChild
            else:
                current.rightChild = Node(value)
                return

def insert_recursive(root, value):
    if root is None:
        root = Node(value)
    else:
        if root.data < value:
            if root.rightChild is None:
                root.rightChild = Node(value)
            else:
                insert_recursive(root.rightChild, value)
        else:
            if root.leftChild is None:
                root.leftChild = Node(value)
            else:
                insert_recursive(root.leftChild, value)
                
def printInorder(root):
    if root:
        printInorder(root.leftChild)
        print(root.data),
        printInorder(root.rightChild) 


def minValueNode(node):
    current = node
    while(current.leftChild is not None):
        current = current.leftChild 
    return current 
 
def deleteNode(root, value):
    if root is None:
        return root 

    if value < root.data:
        root.leftChild = deleteNode(root.leftChild, value)
        
    elif value > root.data:
        root.rightChild = deleteNode(root.rightChild, value)
    # if the value to be deleted is in the root
    else:   
        # one child on right or no child
        if root.leftChild is None :
            temp = root.rightChild 
            root = None
            return temp 

        # if there is a leftChild and no rightChild
        elif root.rightChild is None :
            temp = root.leftChild 
            root = None
            return temp
 
        # Node with two children
        # copy the value of inorder successor of the node to it
        # in order successor is the min value in the right child
        temp = minValueNode(root.rightChild)
 
        # Copy the inorder successor's content to this node
        root.data = temp.data
 
        # Delete the inorder successor
        root.rightChild = deleteNode(root.rightChild , temp.data)
    return root
            
#      50
#    /    \
#   30     70
#   / \    / \
#  20 40  60 80
root = Node(50)
insert_recursive(root, 30)
insert_recursive(root, 20)
insert_recursive(root, 40)
insert_recursive(root,70)
insert(root, 60)
insert(root, 80)
printInorder(root)
print 
print search_recursive(root, 40)
print search_recursive(root, 1)
print search(root, 70)
print search(root, -1)
root = deleteNode(root, 70)
printInorder(root)
