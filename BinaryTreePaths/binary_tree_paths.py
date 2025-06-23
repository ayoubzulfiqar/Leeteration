class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        paths = []

        def dfs(node, current_path):
            if not node:
                return

            # Construct the new path string
            # If current_path is empty (first node), just use node.val
            # Otherwise, append "->" and node.val
            new_path = current_path + (str(node.val) if not current_path else "->" + str(node.val))

            # If it's a leaf node, add the complete path to the results
            if not node.left and not node.right:
                paths.append(new_path)
                return

            # Recursively call for left and right children
            if node.left:
                dfs(node.left, new_path)
            if node.right:
                dfs(node.right, new_path)

        dfs(root, "")
        return paths