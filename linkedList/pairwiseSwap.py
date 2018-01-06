# Given a linked list, swap every two adjacent nodes and return its head.
# e.g. 1->2->3->4 becomes 2->1->4->3

# iterative approach O(n)
def swapPairs(A):
    if A is None:
        return
    current = A
    while current is not None and current.next is not None:
        current.val, current.next.val = current.next.val, current.val
        current = current.next.next
    return A


# recursive O(n)
def swapPairs_recur(A):
    current = A
    if current is not None and current.next is not None:
        current.val, current.next.val = current.next.val, current.val
        current = swapPairs_recur(current.next.next)
    return A

