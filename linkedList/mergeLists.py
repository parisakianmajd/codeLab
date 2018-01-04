# merge two sorted linkedlists

def mergeTwoLists(A, B):
    head1 = A
    head2 = B
    head = ListNode(0)
    temp = head
    
    while head1 and head2:
        if head1.val < head2.val:
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next
    
        temp.next = c          
        temp = temp.next

    temp.next = head1 or head2
    return head.next
