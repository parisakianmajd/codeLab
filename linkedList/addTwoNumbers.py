# Given two linked lists representing two non-negative numbers, in which the digits are stored in reverse order
# and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# e.g. Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


def addTwoNumbers(A, B):
    result = ListNode(0)
    current = result
    carry = 0
    while A is not None or B is not None or carry:
        s = carry
        if A:
            s += A.val
            A = A.next
        if B:
            s += B.val
            B = B.next
        current.next = ListNode(s%10)
        if s >= 10:
            carry = s / 10
        else:
            carry = 0
        
        current = current.next
    return result.next
