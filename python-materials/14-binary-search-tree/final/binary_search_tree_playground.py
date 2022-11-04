#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from binary_search_tree.sources.binary_search_tree import BinarySearchTree
from binary_search_tree.sources.helpers import example_of

bst = BinarySearchTree()
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(0)
bst.insert(2)
bst.insert(5)

example_tree = bst

with example_of("building a BST"):
    print(example_tree)

with example_of("finding a node"):
    if example_tree.contains(5):
        print("Found 5!")
    else:
        print("Couldn't find 5")

with example_of("removing a node"):
    tree = example_tree
    print("Tree before removal:")
    print(tree)
    tree.remove(3)
    print("Tree after removing root:")
    print(tree)
