#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional

from sources.binary_search_tree import BinarySearchTree
from sources.binary_node import BinaryNode

"""
 ### #2. Equatable

 The binary search tree currently lacks `Equatable` conformance. Your challenge is to conform adopt the `Equatable` protocol.
"""

bst1 = BinarySearchTree()
bst1.insert(3)
bst1.insert(1)
bst1.insert(4)
bst1.insert(0)
bst1.insert(2)
bst1.insert(5)

print(f"bst1:\n{bst1}")

bst2 = BinarySearchTree()
bst2.insert(3)
bst2.insert(1)
bst2.insert(4)
bst2.insert(0)
bst2.insert(2)
bst2.insert(5)

print(f"bst2:\n{bst2}")


bst3 = BinarySearchTree()
bst3.insert(3)
bst3.insert(5)
bst3.insert(3)
bst3.insert(1)
bst3.insert(0)
bst3.insert(4)

print(f"bst3:\n{bst3}")


def bst_eq(lhs: BinarySearchTree, rhs: BinarySearchTree) -> bool:
    return is_equal(lhs.root, rhs.root)


def is_equal(left_node: Optional[BinaryNode], right_node: Optional[BinaryNode]) -> bool:
    if left_node is None and right_node is None:
        return True
    elif left_node is None or right_node is None:
        return False
    else:
        return (
            left_node.value == right_node.value
            and is_equal(left_node.left_child, right_node.left_child)
            and is_equal(left_node.right_child, right_node.right_child)
        )


BinarySearchTree.__eq__ = bst_eq

print(f"bst1 == bst2: {bst1 == bst2}, expecting True")
print(f"bst2 == bst3: {bst2 == bst3}, expecting False")
