class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_frequency(head: ListNode) -> dict:
    frequencies = {}
    current = head
    while current:
        frequencies[current.val] = frequencies.get(current.val, 0) + 1
        current = current.next
    return frequencies