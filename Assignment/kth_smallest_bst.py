# kth_smallest_bst.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallest(root, k):
    """
    Find kth smallest element in BST.

    >>> root = TreeNode(3)
    >>> root.left = TreeNode(1)
    >>> root.right = TreeNode(4)
    >>> root.left.right = TreeNode(2)
    >>> kthSmallest(root, 1)
    1
    """
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
