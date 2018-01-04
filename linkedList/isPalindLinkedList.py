#Given a singly linked list, determine if its a palindrome
# in linear time and using a constant space.

# Solution Approach:
# Find length of the list in O(n)
# Find the reverse in O(n)

def isPalind(A):
    if not A or not A.next:
        return True
    current = A
    length = 0
    while current :
        length += 1
        current = current.next
    
    mid = length/2
    temp = A
    prev = None
    for i in xrange(mid):
        prev = temp
        temp = temp.next
    
    prev.next = None
    
    head1 = A
    current = temp
    prev = None
    nextptr = None
    while current:
        nextptr = current.next
        current.next.next = prev
        prev = current
        current = nextptr
    
    head2 = prev
    while head1:
        if head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        else:
            return False
    return True
