# same_tree.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(p, q):
    """
    Check if two trees are exactly the same.

    >>> p = TreeNode(1)
    >>> p.left = TreeNode(2)
    >>> q = TreeNode(1)
    >>> q.left = TreeNode(2)
    >>> isSameTree(p, q)
    True
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
