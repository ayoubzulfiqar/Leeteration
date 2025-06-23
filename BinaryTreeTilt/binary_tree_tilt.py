class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def post_order_traversal_and_sum(node):
            if not node:
                return 0

            left_subtree_sum = post_order_traversal_and_sum(node.left)
            right_subtree_sum = post_order_traversal_and_sum(node.right)

            self.total_tilt += abs(left_subtree_sum - right_subtree_sum)

            return node.val + left_subtree_sum + right_subtree_sum

        post_order_traversal_and_sum(root)
        return self.total_tilt