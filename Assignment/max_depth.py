# max_depth.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    """
    Find maximum depth of a binary tree.
    
    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> maxDepth(root)
    2
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
