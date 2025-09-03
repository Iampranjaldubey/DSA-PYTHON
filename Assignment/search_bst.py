# search_bst.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def searchBST(root, val):
    """
    Search value in BST.

    >>> root = TreeNode(4)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(7)
    >>> searchBST(root, 2).val
    2
    """
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
