import binary_node




class BinaryTree:
    def __init__(self, value):
        self.value = None

    def search(self, root,key):
        if root is None or root.value == key:
            return root

        if root.value < key:
            return self.search(root.right, key)

        return self.search(root.left, key)
    def insert(self, root, key):
        if root is None:
            return self.tree(key)

        else:
            if root.value == key:
                return root
            elif root.value == key:
                return root 
            elif root.value < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
            root 
        

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




