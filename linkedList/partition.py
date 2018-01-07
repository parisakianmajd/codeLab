# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# Example,
# Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5

def partition(head, limit):
    head1 = ListNode(0)
    head2 = ListNode(0)
    left = head1
    right = head2
    current = head
    while current is not None:
        if current.val < limit:
            left.next = current
            left = left.next
        else:
            right.next = current
            right = right.next
        current = current.next
    right.next = None
    if head2.next is not None:
        left.next = head2.next
    return head1.next
