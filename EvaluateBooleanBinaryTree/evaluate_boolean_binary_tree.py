```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root):
    if not root:
        return False
    
    if root.left is None and root.right is None:
        return bool(root.val)
    
    left_val = evaluateTree(root.left)
    right_val = evaluateTree(root.right)
    
    if root.val == 2:
        return left_val or right_val
    elif root.val == 3:
        return left_val and right_val
    else:
        return bool(root.val)
```