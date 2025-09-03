# level_order_traversal.py

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    """
    Level order traversal of a binary tree.

    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> levelOrder(root)
    [[1], [2, 3]]
    """
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
