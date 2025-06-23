class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = self.reverseList(slow.next)

        p1 = head
        p2 = second_half_head
        
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next
        
        return is_palindrome