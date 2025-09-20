# is_bst.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBST(root, left=float('-inf'), right=float('inf')):
    """
    Check if a tree is a BST.

    >>> root = TreeNode(2)
    >>> root.left = TreeNode(1)
    >>> root.right = TreeNode(3)
    >>> isBST(root)
    True
    """
    if not root:
        return True
    if not (left < root.val < right):
        return False
    return isBST(root.left, left, root.val) and isBST(root.right, root.val, right)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
