class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total_sum = 0
        if not root:
            return 0

        stack = [root]

        while stack:
            node = stack.pop()
            
            if not node:
                continue
            
            if low <= node.val <= high:
                total_sum += node.val
            
            if node.val > low:
                stack.append(node.left)
            
            if node.val < high:
                stack.append(node.right)
                
        return total_sum