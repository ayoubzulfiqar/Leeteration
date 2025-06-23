class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        res = []
        stack = []
        curr = root
        last_visited = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack[-1]

            if curr.right and curr.right != last_visited:
                curr = curr.right
            else:
                res.append(stack.pop().val)
                last_visited = curr
                curr = None
        
        return res

    def postorderTraversal_recursive(self, root: TreeNode) -> list[int]:
        res = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)
        
        traverse(root)
        return res

    def postorderTraversal_two_stacks(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        s1 = [root]
        s2 = []
        
        while s1:
            node = s1.pop()
            s2.append(node.val)
            
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        
        return s2[::-1]