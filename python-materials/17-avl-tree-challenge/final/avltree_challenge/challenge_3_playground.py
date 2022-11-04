#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from collections.abc import Callable
from typing import Optional, Protocol, TypeVar

from sources.helpers import example_of
from sources.avl_node import AVLNode
from sources.avl_tree import AVLTree

"""
 ## Challenge 3

 Since there are many iants of binary trees, it makes sense to group shared
 functionality in a protocol. The traversal methods are a good candidate for
 this.

 Create a TraversableBinaryNode protocol that provides a default implementation
 of the traversal methods so that conforming types get these methods for free.
 Have AVLNode conform to this.
"""

Element = TypeVar("Element")


class TraversableBinaryNode(AVLNode):
    pass
    # def value(self) -> Element:
    #     ...

    # def left_child(self) -> Optional[TraversableBinaryNode]:
    #     ...

    # def right_child(self) -> Optional[TraversableBinaryNode]:
    #     ...

    # def traverse_in_order(self, visit: Callable[[Element], None]):
    #     ...

    # def traverse_pre_order(self, visit: Callable[[Element], None]):
    #     ...

    # def traverse_post_order(self, visit: Callable[[Element], None]):
    #     ...

    # These are already in AVLNode
    # def traverse_in_order(self, visit: Callable[[Element], None]) -> None:
    #     self.left_child.traverse_in_order(visit)
    #     visit(self.value)
    #     self.right_child.traverse_in_order(visit)

    # def traverse_pre_order(self, visit: Callable[[Element], None]) -> None:
    #     visit(self.value)
    #     self.left_child.traverse_pre_order(visit)
    #     self.right_child.traverse_pre_order(visit)

    # def traverse_post_order(self, visit: Callable[[Element], None]) -> None:
    #     self.left_child.traverse_post_order(visit)
    #     self.right_child.traverse_post_order(visit)
    #     visit(self.value)


# extension AVLNode: TraversableBinaryNode:
#   pass


# class SpecialAVLTree(AVLTree, TraversableBinaryNode):
#     pass


with example_of("using TraversableBinaryNode"):
    tree = AVLTree()
    for i in range(15):
        tree.insert(i)
    print(tree)
    tree.root.traverse_in_order(lambda x: print(x))

# TODO: assert False
