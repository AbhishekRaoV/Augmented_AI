class TreeNode:
    def __init__(self, value):
        """
        Initialize a new TreeNode with the given value.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        Initialize a new empty BinaryTree.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a new node with the given value into the binary tree.
        Raise ValueError if the value already exists in the tree.
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """
        Helper method to recursively insert a new node with the given value into the binary tree.
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
        Search for a node with the given value in the binary tree.
        Return the node if found, otherwise return None.
        """
        return self._search(self.root, value)

    def _search(self, node, value):
        """
        Helper method to recursively search for a node with the given value in the binary tree.
        """
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)


import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)

    def test_insert(self):
        self.tree.insert(6)
        self.assertIsNotNone(self.tree.search(6))
        with self.assertRaises(ValueError):
            self.tree.insert(4)

    def test_search(self):
        self.assertIsNotNone(self.tree.search(3))
        self.assertIsNone(self.tree.search(8))


if __name__ == '__main__':
    unittest.main()
