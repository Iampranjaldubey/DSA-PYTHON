# delete_bst.py

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def deleteNode(root, key):
    """
    Delete node from BST.

    >>> root = TreeNode(5)
    >>> root.left = TreeNode(3)
    >>> root.right = TreeNode(6)
    >>> root = deleteNode(root, 3)
    >>> root.left
    
    """
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        temp = findMin(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root

def findMin(node):
    while node.left:
        node = node.left
    return node

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
