
import BinaryTreeNode

tree = BinaryTreeNode.BinaryTreeNode(1)
tree.left = BinaryTreeNode.BinaryTreeNode(2)
tree.right = BinaryTreeNode.BinaryTreeNode(3)
tree.left.left = BinaryTreeNode.BinaryTreeNode(4)

print("In order Traversal:\n", end='')
tree.traverseInOrder()

print("\nPre order Traversal:\n", end='')
tree.traversePreOrder()
print("\nPost order Traversal:\n", end='')
tree.traversePostOrder()



