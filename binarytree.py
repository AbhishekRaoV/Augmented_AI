class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            # Value already exists, raise ValueError
            raise ValueError("Value already exists in the tree")
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)


# Test cases using unittest
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
