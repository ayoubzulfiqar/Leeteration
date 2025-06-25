```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkTree(root: TreeNode) -> bool:
    if root is None or root.left is None or root.right is None:
        return False
    return root.val == root.left.val + root.right.val
```