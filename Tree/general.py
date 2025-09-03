class Node:
    """
    Node of a Binary Search Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree with insert, search, delete, and inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert data into the BST.
        """
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        """
        Search for a value in the BST.
        """
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder(self):
        """
        Inorder traversal of BST (ascending order).
        """
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def delete(self, data):
        """
        Delete a node with the given value from BST.
        """
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            min_larger_node = self._min_value_node(node.right)
            node.data = min_larger_node.data
            node.right = self._delete(node.right, min_larger_node.data)

        return node

    def _min_value_node(self, node):
        """
        Get the node with the minimum value (used in deletion).
        """
        current = node
        while current.left:
            current = current.left
        return current
