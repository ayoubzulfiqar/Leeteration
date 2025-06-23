# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min1 = root.val
        min2 = float('inf')

        def dfs(node):
            nonlocal min2
            if not node:
                return

            # Pruning condition: if current node's value is already greater than or equal to our current second minimum candidate,
            # then its children will also have values greater than or equal to node.val (due to the tree property
            # root.val = min(root.left.val, root.right.val)), so they won't yield a smaller second minimum.
            if node.val >= min2:
                return

            # If node.val is greater than the absolute minimum (min1), it's a candidate for min2.
            # Since we already pruned if node.val >= min2, this means node.val must be strictly less than current min2.
            # So, we can directly update min2.
            if node.val > min1:
                min2 = node.val
            
            # Recursively explore children.
            # We must explore children if node.val == min1, because they might contain values greater than min1.
            # We also explore children if node.val is a candidate for min2 (i.e., min1 < node.val < min2),
            # because its children might also contain values equal to min1, or other candidates for min2.
            # The pruning `if node.val >= min2` effectively controls which branches are explored.
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # If min2 is still infinity, it means no value greater than min1 was found.
        if min2 == float('inf'):
            return -1
        else:
            return min2