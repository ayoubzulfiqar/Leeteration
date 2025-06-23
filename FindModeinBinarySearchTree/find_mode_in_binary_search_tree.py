from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []

        def inorder_traverse(node):
            if not node:
                return

            inorder_traverse(node.left)

            if self.current_val is None or node.val != self.current_val:
                self.current_val = node.val
                self.current_count = 1
            else:
                self.current_count += 1

            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [self.current_val]
            elif self.current_count == self.max_count:
                self.modes.append(self.current_val)

            inorder_traverse(node.right)

        inorder_traverse(root)
        return self.modes