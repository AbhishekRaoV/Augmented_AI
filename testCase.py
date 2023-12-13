import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)

    def test_search_existing_value(self):
        result = self.tree.search(4)
        self.assertEqual(result.value, 4)

    def test_search_non_existing_value(self):
        result = self.tree.search(9)
        self.assertIsNone(result)

    def test_insert_existing_value(self):
        with self.assertRaises(ValueError):
            self.tree.insert(5)

if __name__ == '__main__':
    unittest.main()
