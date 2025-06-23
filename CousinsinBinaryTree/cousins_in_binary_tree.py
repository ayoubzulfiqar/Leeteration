import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([(root, None, 0)])
        x_info = None
        y_info = None

        while queue:
            current_node, parent_node, depth = queue.popleft()

            if current_node.val == x:
                x_info = (parent_node, depth)
            elif current_node.val == y:
                y_info = (parent_node, depth)

            if x_info and y_info:
                break

            if current_node.left:
                queue.append((current_node.left, current_node, depth + 1))
            if current_node.right:
                queue.append((current_node.right, current_node, depth + 1))
        
        return x_info[1] == y_info[1] and x_info[0] != y_info[0]