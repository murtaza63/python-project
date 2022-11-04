#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from binary_node import BinaryNode
from comparable import Comparable

Element = TypeVar("Element", bound=Comparable)


class BinarySearchTree(Generic[Element]):
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def __str__(self) -> str:
        if not self.root:
            return "empty tree"
        return str(self.root)

    def insert(self, value: Element) -> None:
        self.root = self.insert_from_node(self.root, value)

    def insert_from_node(self, node: Optional[BinaryNode], value: Element) -> BinaryNode:
        if not node:
            return BinaryNode(value=value)
        if value < node.value:
            node.left_child = self.insert_from_node(node.left_child, value)
        else:
            node.right_child = self.insert_from_node(node.right_child, value)
        return node

    def contains(self, value: Element) -> bool:
        current = self.root
        while node := current:
            if node.value == value:
                return True
            if value < node.value:
                current = node.left_child
            else:
                current = node.right_child
        return False

    def remove(self, value: Element) -> None:
        self.root = self.remove_node_with_value(self.root, value)

    def remove_node_with_value(self, node: Optional[BinaryNode], value: Element) -> Optional[BinaryNode]:
        if not node:
            return None
        if value == node.value:
            if node.left_child is None and node.right_child is None:
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child

            node.value = self.minNode(node.right_child).value
            node.right_child = self.remove_node_with_value(node.right_child, node.value)
        elif value < node.value:
            node.left_child = self.remove_node_with_value(node.left_child, value)
        else:
            node.right_child = self.remove_node_with_value(node.right_child, value)
        return node

    def minNode(self, node: BinaryNode) -> BinaryNode:
        if not node.left_child:
            return node
        else:
            return self.minNode(node.left_child)
