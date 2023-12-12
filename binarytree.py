def insert(self, value):
    self.root = self._insert(self.root, value)

def _insert(self, node, value):
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = self._insert(node.left, value)
    elif value > node.value:
        node.right = self._insert(node.right, value)
    return node
def test_insert(self):
    self.tree.insert(6)
    self.assertIsNotNone(self.tree.search(6))
    self.assertIsNone(self.tree.insert(4))
def test_search(self):
    self.assertIsNotNone(self.tree.search(3))
    self.assertIsNone(self.tree.search(8))
