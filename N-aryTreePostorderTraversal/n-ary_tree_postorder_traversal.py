class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result = []
        if root is None:
            return result

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            for child in node.children:
                stack1.append(child)
        
        while stack2:
            result.append(stack2.pop().val)
            
        return result