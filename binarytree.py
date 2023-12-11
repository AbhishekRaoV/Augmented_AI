class TreeNode:
    """
    Represents a node in a binary search tree.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the TreeNode class.
        """
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Represents a binary search tree.
    """

    def __init__(self):
        """
        Initializes a new instance of the BinarySearchTree class.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary search tree.
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """
        Helper method to recursively insert a value into the binary search tree.
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
        Searches for a value in the binary search tree.
        Returns True if the value is found, False otherwise.
        """
        return self._search(self.root, value)

    def _search(self, node, value):
        """
        Helper method to recursively search for a value in the binary search tree.
        """
        if node is None:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)


import unittest


class TestBinarySearchTree(unittest.TestCase):
    """
    Test cases for the BinarySearchTree class.
    """

    def test_insert(self):
        """
        Test case for the insert method.
        """
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)

        # Inserting a value that already exists should raise a ValueError
        with self.assertRaises(ValueError):
            tree.insert(4)

        # Inserting a new value should not raise an exception
        tree.insert(6)
        self.assertTrue(tree.search(6))

    def test_search(self):
        """
        Test case for the search method.
        """
        tree = BinarySearchTree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)
        tree.insert(2)
        tree.insert(4)

        # Searching for an existing value should return True
        self.assertTrue(tree.search(3))

        # Searching for a non-existing value should return False
        self.assertFalse(tree.search(8))


if __name__ == '__main__':
    unittest.main()
