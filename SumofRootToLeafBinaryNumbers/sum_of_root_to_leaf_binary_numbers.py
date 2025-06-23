class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total_sum = 0

        def dfs(node, current_val):
            nonlocal total_sum
            if not node:
                return

            current_val = (current_val << 1) | node.val

            if not node.left and not node.right:
                total_sum += current_val
                return

            dfs(node.left, current_val)
            dfs(node.right, current_val)

        dfs(root, 0)
        return total_sum