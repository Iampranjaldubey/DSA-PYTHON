# insert_bst.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertBST(root, val):
    """
    Insert value in BST.

    >>> root = TreeNode(4)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(7)
    >>> new_root = insertBST(root, 5)
    >>> new_root.right.left.val
    5
    """
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertBST(root.left, val)
    else:
        root.right = insertBST(root.right, val)
    return root

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
