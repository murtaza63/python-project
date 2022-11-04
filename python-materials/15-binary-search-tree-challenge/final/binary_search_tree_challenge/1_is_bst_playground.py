#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


from typing import Optional, TypeVar

Element = TypeVar("Element")


from typing import Optional
from sources.binary_search_tree import BinarySearchTree
from sources.binary_node import BinaryNode

"""
 # Binary Search Tree Challenges
 ### #1. Binary Tree or Binary Search Optional[Tree]
 Create a function that checks if a binary tree is a binary search tree.
"""

bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(0)
bst.insert(2)
bst.insert(5)

print(bst)


def is_binary_search_tree(tree: BinaryNode) -> bool:
    return is_bst(tree, float("-inf"), float("inf"))


def is_bst(tree: Optional[BinaryNode], min: float, max: float) -> bool:
    if not tree:
        return True

    return min <= tree.value <= max and is_bst(tree.left_child, min, tree.value) and is_bst(tree.right_child, tree.value, max)


print(is_binary_search_tree(bst.root))
