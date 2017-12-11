# -*- coding: utf-8 -*-
#Find the node at which the intersection of two singly linked lists begins.
#e.g. In the following example, c1 is the insertion point
#A:          a1 → a2
#                   ↘
#                     c1 → c2 → c3
#                   ↗
#B:     b1 → b2 → b3


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getLen(A):
    l = 0
    current = A
    if not current:
        return 0
    while current:
        l += 1
        current = current.next
    return l
def getIntersectionNode(A, B):
    if A is None or B is None:
        return
    m = getLen(A)
    n = getLen(B)
    d = abs(n-m)
    if n > m:
        A, B = B, A
    currentA = A
    currentB = B
    for i in xrange(d):
        currentA = currentA.next
    while currentA != currentB and currentA != None:
            currentA = currentA.next
            currentB = currentB.next
            
    return currentA
