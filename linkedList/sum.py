#given two linked lists representing two non-negative numbers.
#The digits are stored in reverse order and each of their nodes contain
#a single digit. Add the two numbers and return it as a linked list.
# Python program to add two numbers represented by linked list
 
class Node: 
    def __init__(self, val):
        self.data = val
        self.next = None
 
class LinkedList:
     def __init__(self):
        self.head = None

     # push to the front of the linkedist
     def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

     def addTwoLists(self, first, second):
         carry = 0
         prev = None
         
         while first is not None or second is not None:
             fdata = 0 if first is None else first.data
             sdata = 0 if second is None else second.data
             Sum = carry + fdata + sdata
             carry = 1 if Sum >= 10 else 0
             Sum = Sum if Sum < 10 else Sum % 10
             temp = Node(Sum)
             if self.head is None:
                 self.head = temp
             else:
                 prev.next = temp 
             prev = temp
             # Move first and second pointers to next nodes
             if first is not None:
                 first = first.next
             if second is not None:
                 second = second.next
         if carry > 0:
            temp.next = Node(carry)
     def printList(self):
         temp = self.head
         while(temp):
             print temp.data,
             temp = temp.next
 
first = LinkedList()
second = LinkedList()
 
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print "First List is ",
first.printList()
 
second.push(4)
second.push(8)
print "\nSecond List is ",
second.printList()
 
res = LinkedList()
res.addTwoLists(first.head, second.head)
print "\nResultant list is ",
res.printList()
       
       
        
        

