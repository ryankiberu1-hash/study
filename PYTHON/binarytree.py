class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Test traversal
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
inorder(root)


