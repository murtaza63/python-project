import BinaryTreeNode

tree = BinaryTreeNode.BinaryTreeNode(1)
tree.left = BinaryTreeNode.BinaryTreeNode(2)
tree.right = BinaryTreeNode.BinaryTreeNode(3)
tree.left.left = BinaryTreeNode.BinaryTreeNode(4)
tree.left.right = BinaryTreeNode.BinaryTreeNode(5)

def serilize(root):
    arr = []
    def dfs(node):
        if not node:
            arr.append("N")
        arr.append(str(node.value))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(arr)

print(serilize(tree)) 