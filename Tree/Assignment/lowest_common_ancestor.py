# lowest_common_ancestor.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    Find lowest common ancestor in BST.

    >>> root = TreeNode(6)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(8)
    >>> lowestCommonAncestor(root, root.left, root.right).val
    6
    """
    if not root:
        return None
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    return root

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
