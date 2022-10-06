
import BinaryTreeNode

tree = BinaryTreeNode.BinaryTreeNode(1)
tree.left = BinaryTreeNode.BinaryTreeNode(2)
tree.right = BinaryTreeNode.BinaryTreeNode(3)
tree.left.left = BinaryTreeNode.BinaryTreeNode(4)
tree.left.right = BinaryTreeNode.BinaryTreeNode(5)



def height(root)-> int:
    if root is None:
        return 0
    leftChild = height(root.left)
    rightChild = height(root.right)
    return max(leftChild, rightChild) + 1

   


print("The height of binary tree is:",height(tree))