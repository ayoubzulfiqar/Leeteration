class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest_val = root.val
        min_diff = abs(root.val - target)

        current = root
        while current:
            current_diff = abs(current.val - target)

            if current_diff < min_diff:
                min_diff = current_diff
                closest_val = current.val
            
            if current.val == target:
                return current.val

            if target < current.val:
                current = current.left
            else:
                current = current.right
        
        return closest_val