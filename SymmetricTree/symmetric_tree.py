import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricRecursive(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            return isMirror(node1.left, node2.right) and \
                   isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)

    def isSymmetricIterative(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = collections.deque()
        queue.append((root.left, root.right))

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True