class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root: TreeNode) -> list[int]:
        lonely_nodes = []

        def dfs(node):
            if not node:
                return

            # If node has a left child but no right child, the left child is lonely
            if node.left and not node.right:
                lonely_nodes.append(node.left.val)
            # If node has a right child but no left child, the right child is lonely
            elif node.right and not node.left:
                lonely_nodes.append(node.right.val)
            
            # Recursively call for left and right children
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return lonely_nodes