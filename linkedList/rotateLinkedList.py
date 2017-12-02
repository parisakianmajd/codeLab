#Given a list, rotate the list to the right by k places, where k is non-negative.

#For example:

#Given 1->2->3->4->5->NULL and k = 2,
#return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        left = right = A
        count = 0
        while count < B:
            right = right.next
            if right == None:
                right = A
            count += 1
        while right.next is not None:
            left = left.next
            right = right.next
        right.next = A
        head = left.next
        left.next = None
        return head
