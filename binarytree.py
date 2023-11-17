clas TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result += inorder_traversal(root.right)
    return result


def preorder_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result


def postorder_traversal(root):
    result = []
    if root:
        result = postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.val)
    return result


# Example usage:
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

print("In-order traversal:", inorder_traversal(root))
print("Pre-order traversal:", preorder_traversal(root))
print("Post-order traversal:", postorder_traversal(root))
