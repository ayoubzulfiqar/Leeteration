from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        current = head

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
        
        return dummy.next