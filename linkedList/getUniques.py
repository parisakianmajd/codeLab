
#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

#For example,
#Given 1->2->3->3->4->4->5, return 1->2->5.
def deleteDuplicates(A):
      current = ret = A
        prev = None
        while current is not None:
            c = 0
            val = current.val
            while current is not None and current.val == val:
                current = current.next
                c += 1
            if c == 1:
                ret.val = val
                prev = ret 
                ret = ret.next
                
        if prev:
            prev.next = None
        else:
            A = None
        return A
