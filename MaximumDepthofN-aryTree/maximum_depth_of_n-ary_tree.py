from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_depth = 0

        while queue:
            current_node, current_depth = queue.popleft()
            max_depth = max(max_depth, current_depth)

            for child in current_node.children:
                queue.append((child, current_depth + 1))

        return max_depth