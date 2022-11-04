#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from binary_trees.sources.binary_node import BinaryNode
from binary_trees.sources.helpers import example_of

# TODO: Figure out how to get this to work
# from src.helpers import example_of

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

with example_of("tree diagram"):
    print(tree)

with example_of("in-order traversal"):
    tree.traverse_in_order(lambda node: print(node))

with example_of("pre-order traversal"):
    tree.traverse_pre_order(lambda node: print(node))

with example_of("post-order traversal"):
    tree.traverse_post_order(lambda node: print(node))
