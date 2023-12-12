class TreeNode:
    def __init__(self, value):
        """
        Initialize a new TreeNode object.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        Initialize a new BinaryTree object.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a value into the binary tree.

        Args:
            value: The value to be inserted.

        Raises:
            ValueError: If the value already exists in the tree.
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """
        Helper method to recursively insert a value into the binary tree.

        Args:
            node: The current node being checked.
            value: The value to be inserted.

        Returns:
            The updated node.

        Raises:
            ValueError: If the value already exists in the tree.
        """
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            raise ValueError("Value already exists in the tree")
        return node

    def search(self, value):
        """
        Search for a value in the binary tree.

        Args:
            value: The value to search for.

        Returns:
            The node containing the value, or None if not found.
        """
        return self._search(self.root, value)

    def _search(self, node, value):
        """
        Helper method to recursively search for a value in the binary tree.

        Args:
            node: The current node being checked.
            value: The value to search for.

        Returns:
            The node containing the value, or None if not found.
        """
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)


import unittest


class TestBinaryTree(unittest.TestCase):
    def test_insert(self):
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        self.assertIsNotNone(tree.search(6))
        with self.assertRaises(ValueError):
            tree.insert(4)

    def test_search(self):
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)
        self.assertIsNotNone(tree.search(3))
        self.assertIsNone(tree.search(8))


if __name__ == '__main__':
    unittest.main()
