
# Bubble Sort

def sortList(A):
    if A is None or A.next is None:
        return A
    head = A
    sorted = False
    while not sorted:
        sorted = True
        prev = head
        current = head.next
        while current is not None:
            if prev.val > current.val:
                    sorted = False
                    prev.val, current.val = current.val, prev.val
            prev = current
            current = current.next
    return head
