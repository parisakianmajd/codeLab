class Node:
    def __init__(self, val = None,):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, node):
        self.node = node

    def __str__(self):
        current = self.node
        outStr = "[" + str(current.val)
        if current.next is None:
            return outStr + "]"
        while current.next is not None:
            outStr += ', ' + str(current.next.val)
            current = current.next
        return outStr + "]"
            
    def add(self, newNode):
        current = self.node
        while current.next is not None:
            current = current.next
        current.next = newNode
        
    # Given a specific value, delete every node of the linkedlist containing that value.
    def delete(self, value):
        head = self.node
        
        # if the head itself has the value or multiple occurances of it
        while head is not None and head.val == value:
            head = head.next           
        if not head:
            return
        current = head
        while current.next is not None:
            if current.next.val == value:
                current.next = current.next.next
            else:
                current = current.next
        self.node = head
        return self

ll = LinkedList(Node(1))
ll.add(Node(21))
ll.add(Node(21))
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(2))
ll.add(Node(3))
ll.add(Node(5))
ll.add(Node(8))
ll.add(Node(13))
ll.add(Node(21))
print str(ll)
ll.delete(1)
print str(ll)
ll.delete(21)
print str(ll)
ll.delete(2)
print str(ll)



