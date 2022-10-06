import BinaryTreeNode
import unittest

class TestBTree(unittest.TestCase):
    def test_preorder(self):
        tree = BinaryTreeNode.BinaryTreeNode(1)
        tree.left = BinaryTreeNode.BinaryTreeNode(2)
        tree.right =BinaryTreeNode.BinaryTreeNode(3)
        self.assertEqual(tree.traversePreOrder(), 1)
        

