#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from avl_tree.sources.avl_tree import AVLTree
from avl_tree.sources.helpers import example_of

with example_of("repeated insertions in sequence"):
    tree = AVLTree()
    for i in range(15):
        tree.insert(i)
    print(tree)

with example_of("removing a value"):
    tree = AVLTree()
    tree.insert(15)
    tree.insert(10)
    tree.insert(16)
    tree.insert(18)
    print(tree)
    tree.remove(10)
    print(tree)
