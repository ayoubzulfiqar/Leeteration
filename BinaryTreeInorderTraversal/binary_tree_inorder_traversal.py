class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        # Recursive Solution
        # def _inorder_recursive(node):
        #     if not node:
        #         return
        #     _inorder_recursive(node.left)
        #     result.append(node.val)
        #     _inorder_recursive(node.right)
        
        # _inorder_recursive(root)
        # return result

        # Iterative Solution
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result