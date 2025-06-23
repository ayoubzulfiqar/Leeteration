class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: 'Optional[TreeNode]') -> int:
        if not root:
            return 0

        def dfs(current_node: 'Optional[TreeNode]', is_left_child: bool) -> int:
            if not current_node:
                return 0

            if not current_node.left and not current_node.right:
                if is_left_child:
                    return current_node.val
                else:
                    return 0

            left_sum = dfs(current_node.left, True)
            right_sum = dfs(current_node.right, False)

            return left_sum + right_sum

        return dfs(root, False)