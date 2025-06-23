class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.new_head = None
        self.prev = None

        def inorder_traverse(node):
            if not node:
                return

            inorder_traverse(node.left)

            if not self.new_head:
                self.new_head = node
            else:
                self.prev.right = node

            node.left = None
            self.prev = node

            inorder_traverse(node.right)

        inorder_traverse(root)
        return self.new_head