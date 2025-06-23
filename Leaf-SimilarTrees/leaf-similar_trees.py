class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def _get_leaf_sequence(node: TreeNode, leaves: list):
            if not node:
                return
            
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            
            _get_leaf_sequence(node.left, leaves)
            _get_leaf_sequence(node.right, leaves)

        leaves1 = []
        leaves2 = []

        _get_leaf_sequence(root1, leaves1)
        _get_leaf_sequence(root2, leaves2)

        return leaves1 == leaves2