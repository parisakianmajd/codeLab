# remove the nth element from a linkedlist

class Solution:
    def list_len(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def remove_nth(self, head, n):
        if n == 0:
            return head.next
        current = head
        for _ in xrange(n-1):
            current = current.next
        current.next = current.next.next
        return head
        
    def removeNthFromEnd(self, head, rmv):
        length = self.list_len(head)
        ind = length - rmv
        if not (0 <= ind < length):
            return head.next
        return self.remove_nth(head, ind)
