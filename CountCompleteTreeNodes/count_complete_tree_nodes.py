class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, node: TreeNode) -> int:
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)

        if h_left == h_right:
            return (1 << h_left) + self.countNodes(root.right)
        else:
            return (1 << h_right) + self.countNodes(root.left)