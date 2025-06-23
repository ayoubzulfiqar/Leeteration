class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        result = []
        if not root:
            return result

        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push children onto the stack in reverse order
            # so that the leftmost child is processed first (LIFO stack behavior)
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])
        
        return result