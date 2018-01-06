# Reverse a linked list from position m to n. Do it in-place and in one-pass.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        
    def add(self, val):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val)
        
    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
    
    #reverse every k nodes
    def reverseK(self, head, k):
        current = head 
        nextNode  = None
        prev = None
        count = 0
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        # next is a pointer to k+1th node
        # recursive call 
        if nextNode is not None:
            head.next = self.reverse(nextNode, k)
        # prev is new head
        return prev    
    #reverse every k nodes
       def reverseK2(self, head, k):
        if head == None or head.next == None:
            return head
        nextNode = prev = None
        
        current = head
        prevHead = None
        currHead = current
        while current is not None:
            currHead = current
            count = 0
            prev = None
            while current is not None and count < k:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
                count += 1
            if prevHead != None:
                prevHead.next = prev
            else:
                head = prev
            prevHead = currHead
        return head
     
    # Reverse a linked list from position m to n          
    def reverseBetween(self, head, m,n):
        if n == m:
            return head
        start = None
        startPrev = None
        end = None
        endNext = None
        current = head
        count = 1
        while current and count <= n:
            if count < m:
                startPrev = current
            if count == m:
                start = current
            if count == n:
                end = current
                endNext = current.next               
            current = current.next
            count += 1
        
        end.next = None  # this is to close the end and reverse the substring
        end = self.reverse(start)
        if startPrev:
            startPrev.next = end
        else:
            head = end
        start.next = endNext
        return head
          
        
    def __str__(self):
        current = self.head
        outStr = "[" + str(current.val)
        if current.next is None:
            return outStr + "]"
        while current.next is not None:
            outStr += ', ' + str(current.next.val)
            current = current.next
        return outStr + "]"


llist = LinkedList(Node(0))
llist.add(20)
llist.add(4)
llist.add(15)
llist.add(85)
print str(llist)
llist.head = llist.reverse(llist.head)
print str(llist)
llist.head= llist.reverseBetween(llist.head, 2,3)
print str(llist)
