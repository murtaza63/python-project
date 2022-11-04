#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional

from sources.binary_node import BinaryNode

"""
 # Binary Tree Challenges

 ## #1. Height of a Tree

 Given a binary tree, find the height of the tree. The height of the binary tree
 is determined by the distance between the root and the furthest leaf. The
 height of a binary tree with a single node is zero, since the single node is
 both the root and the furthest leaf.
"""

zero = BinaryNode(value=0)
one = BinaryNode(value=1)
five = BinaryNode(value=5)
seven = BinaryNode(value=7)
eight = BinaryNode(value=8)
nine = BinaryNode(value=9)

seven.left_child = one
one.left_child = zero
one.right_child = five
seven.right_child = nine
nine.left_child = eight

tree = seven

print(tree)

# 1. Find the height of the binary tree.


def height_of_node(node: Optional[BinaryNode]) -> int:
    if not node:
        return -1
    return 1 + max(height_of_node(node.left_child), height_of_node(node.right_child))


height = height_of_node(tree)
print(f"height: {height}")
