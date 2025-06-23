class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen_values = set()

        def dfs(node):
            if not node:
                return False

            if dfs(node.left):
                return True

            complement = k - node.val
            if complement in seen_values:
                return True
            seen_values.add(node.val)

            if dfs(node.right):
                return True

            return False

        return dfs(root)