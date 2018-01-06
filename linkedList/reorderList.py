# Given a singly linked list
# L: L0 -> L1 -> ... -> Ln-1 -> Ln,
# reorder it to:
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
def reverseList(head):
    current = head
    prev = None
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev

def reorderList(A):
    # find the middle point and break the linkedlist to two halfs
    # reverse the 2nd half
    # while merging the halfs alternate the nodes


    # use tortoise and hare method to find the middle
    # the slow pointer traverses the nodes one by one and the fast moves at steps of two
    # when the fast reaches the end, the slow is at the middle
    slow = A
    fast = A.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    
    # split
    node1 = A
    node2 = slow.next
    slow.next = None
    
    # reverse the 2nd half
    node2 = reverseList(node2)
    
    # merge
    node = ListNode(0) # dummy node
    current = node
    while node1 is not None or node2 is not None:
        if node1 is not None:
            current.next = node1
            current = current.next
            node1 = node1.next
        if node2 is not None:
            current.next = node2
            current = current.next
            node2 = node2.next
    return node.next # remove dummy node
