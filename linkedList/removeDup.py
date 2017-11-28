# Given a sorted linkedlist, remove all duplicates
class Node:
    def __init__(self, val=None, next = None):
        self.val = val
        self.next= next
        
class LinkedList:
    def __init__(self, head):
        self.head = head

    def add(self, newNode):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode

        
    def __str__(self):
        out = []
        if not self.head:
            return
        current = self.head
        while current.next is not None:
            out.append(current.next.val)
            current = current.next
        return ', '.join(map(str,out))

    def removeDup(self):
        if not self.head:
            return self.head
        current = self.head
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return self

head = Node()
ll = LinkedList(head)
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(1))
ll.add(Node(2))
ll.add(Node(2))
ll.add(Node(5))
ll.add(Node(8))
ll.add(Node(8))
ll.add(Node(21))
print str(ll)
ll.removeDup()
print str(ll)

