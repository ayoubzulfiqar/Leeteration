class RopeTreeNode:
    def __init__(self, val=None, length=0, left=None, right=None):
        self.val = val
        self.length = length
        self.left = left
        self.right = right


class Solution:
    def getKthCharacter(self, root: 'RopeTreeNode', k: int) -> str:
        current = root
        while current:
            if current.val is not None:
                return current.val[k - 1]
            else:
                left_subtree_length = current.length
                if k <= left_subtree_length:
                    current = current.left
                else:
                    k -= left_subtree_length
                    current = current.right
        return ""