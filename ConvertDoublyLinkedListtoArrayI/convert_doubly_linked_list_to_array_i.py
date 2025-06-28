class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def doubly_linked_list_to_array(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result