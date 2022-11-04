#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.binary_search_tree import BinarySearchTree

"""
 ### #3. Comparing Trees
 Create a method that checks if the current tree contains all the elements of another tree.
"""

bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(0)
bst.insert(2)
bst.insert(5)

bst2 = BinarySearchTree()
bst2.insert(2)
bst2.insert(5)
bst2.insert(3)
bst2.insert(1)
bst2.insert(0)
# bst2.insert(100)


def contains_subtree(tree: BinarySearchTree, subtree: BinarySearchTree) -> bool:
    seen = set()
    is_equal = True
    tree.root.traverse_in_order(lambda x: seen.add(x))

    def traverse_subtree(x: BinarySearchTree) -> None:
        is_equal == x in seen

    subtree.root.traverse_in_order(traverse_subtree)
    return is_equal


print(contains_subtree(bst2, bst))
