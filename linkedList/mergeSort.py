# Merge Sort

def sortList(A):
    # handling base cases of length = 0, 1 and 2
    if A is None or A.next is None:
        return A
    if A.next.next is None:
        n1 = A
        n2 = A.next
        if n1.val > n2.val:
            n2.next = n1
            n1.next = None
            return n2
        return n1
    # use fast and slow pointers to find the middle point
    slow = A
    fast = A.next.next
    while fast.next and fast.next.next:
        slow= slow.next
        fast=fast.next.next
    
    x1 = A
    x2 = slow.next
    slow.next = None
    
    # recursively call for each half
    
    s1 = sortList(x1)
    s2 = sortList(x2)
    
    result = ListNode(0)
    current = start
    
    # merge both sorted parts together
    
    while s1 and s2:
        if s1.val < s2.val:
            current.next = s1
            s1 = s1.next
        else:
            current.next = s2
            s2 = s2.next
        current = current.next
    if s1:
        current.next = s1
    if s2:
        current.next = s2
    return result.next
