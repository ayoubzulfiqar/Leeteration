class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current:
            keep_ptr = current
            for _ in range(m):
                if not keep_ptr:
                    break
                keep_ptr = keep_ptr.next
            
            if not keep_ptr:
                break

            delete_ptr = keep_ptr.next
            for _ in range(n):
                if not delete_ptr:
                    break
                delete_ptr = delete_ptr.next
            
            keep_ptr.next = delete_ptr
            current = delete_ptr

        return dummy.next