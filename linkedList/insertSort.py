# Insert Sort

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# insert a new node to into a sorted list
def sortedInsert(head, newNode):
     
    if head is None:
        newNode.next = None
        head = newNode  
        
    elif head.val >= newNode.val:
        # if the list is empty put the newNode as head
        # Or if the newnNode is smaller than head
        newNode.next = head
        head = newNode
        
    else :
        # Locate the node before the point of insertion
        current = head
        while current.next is not None and current.next.val < newNode.val:
            current = current.next
        newNode.next = current.next
        current.next = newNode
    return head
    
def insertionSortList(A):
    if A is None or A.next is None:
        return A
    sortedList = None
    current = A
    while current is not None:
        nextNode = current.next
        sortedList = sortedInsert(sortedList, current)
        current = nextNode
    return sortedList
