class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        Inserts a value into the binary tree.
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node: TreeNode, value: int) -> TreeNode:
        """
        Helper method to recursively insert a value into the binary tree.
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

    def search(self, value: int) -> bool:
        """
        Searches for a value in the binary tree.
        Returns True if the value is found, False otherwise.
        """
        return self._search(self.root, value)

    def _search(self, node: TreeNode, value: int) -> bool:
        """
        Helper method to recursively search for a value in the binary tree.
        Returns True if the value is found, False otherwise.
        """
        if node is None or node.value == value:
            return node is not None
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
        self.assertTrue(tree.search(3))
        self.assertFalse(tree.search(8))
        self.assertFalse(tree.search(6))


if __name__ == '__main__':
    unittest.main()
