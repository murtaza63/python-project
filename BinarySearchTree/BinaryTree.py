import binary_node

tree = binary_node.BinaryNode(1)
tree.left = binary_node.BinaryNode(2)
tree.right = binary_node.BinaryNode(3)
tree.left.left = binary_node.BinaryNode(4)

print("In order Traversal:\n", end='')
tree.traverseInOrder()

print("\nPre order Traversal:\n", end='')
tree.traversePreOrder()
print("\nPost order Traversal:\n", end='')
tree.traversePostOrder()

print("root is :",tree.printTree())