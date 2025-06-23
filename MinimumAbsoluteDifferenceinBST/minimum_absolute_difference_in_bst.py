class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.prev_val = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        self._inorder_traverse(root)
        return self.min_diff

    def _inorder_traverse(self, node: TreeNode):
        if not node:
            return

        self._inorder_traverse(node.left)

        if self.prev_val is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev_val)
        self.prev_val = node.val

        self._inorder_traverse(node.right)