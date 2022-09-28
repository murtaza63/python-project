from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)
root.left.left = Node(9)
root.left.right = Node(11)

print("Binary Tree:", root)

print("List of nodes :", list(root))

print("Inorder of nodes:", root.inorder)
print("Preorder of nodes:", root.preorder)

print("Postorder of nodes:", root.postorder)

print("Size of tree:", root.size)

print("Height of tree:", root.height)

print("Properties: \n", root.properties)

print("Is balance Binary Tree: \n", root.is_balanced)

