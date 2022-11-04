#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from avl_node import AVLNode
from comparable import Comparable

Element = TypeVar("Element", bound=Comparable)


class AVLTree(Generic[Element]):
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def __str__(self) -> str:
        if not self.root:
            return "empty tree"
        return str(self.root)

    def insert(self, value: Element) -> None:
        self.root = self.insert_from_node(self.root, value)

    def insert_from_node(self, node: Optional[AVLNode], value: Element) -> AVLNode:
        if not node:
            return AVLNode(value=value)
        if value < node.value:
            node.left_child = self.insert_from_node(node.left_child, value)
        else:
            node.right_child = self.insert_from_node(node.right_child, value)
        balanced_node = self.balanced(node)
        balanced_node.height = max(balanced_node.left_height, balanced_node.right_height) + 1
        return balanced_node

    def left_rotate(self, node: AVLNode) -> AVLNode:
        assert node.right_child is not None
        pivot = node.right_child
        node.right_child = pivot.left_child
        pivot.left_child = node
        node.height = max(node.left_height, node.right_height) + 1
        pivot.height = max(pivot.left_height, pivot.right_height) + 1
        return pivot

    def right_rotate(self, node: AVLNode) -> AVLNode:
        assert node.left_child is not None
        pivot = node.left_child
        node.left_child = pivot.right_child
        pivot.right_child = node
        node.height = max(node.left_height, node.right_height) + 1
        pivot.height = max(pivot.left_height, pivot.right_height) + 1
        return pivot

    def right_left_rotate(self, node: AVLNode) -> AVLNode:
        right_child = node.right_child
        if not right_child:
            return node
        node.right_child = self.right_rotate(right_child)
        return self.left_rotate(node)

    def left_right_rotate(self, node: AVLNode) -> AVLNode:
        left_child = node.left_child
        if not left_child:
            return node
        node.left_child = self.left_rotate(left_child)
        return self.right_rotate(node)

    def balanced(self, node: AVLNode) -> AVLNode:
        balance_factor: int = node.balance_factor
        # TODO: use match balance_factor:
        if balance_factor == 2:
            left_child = node.left_child
            if left_child and left_child.balance_factor == -1:
                return self.left_right_rotate(node)
            else:
                return self.right_rotate(node)
        elif balance_factor == -2:
            right_child = node.right_child
            if right_child and right_child.balance_factor == 1:
                return self.right_left_rotate(node)
            else:
                return self.left_rotate(node)
        else:
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

    def remove_node_with_value(self, node: Optional[AVLNode], value: Element) -> Optional[AVLNode]:
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
        balanced_node = self.balanced(node)
        balanced_node.height = max(balanced_node.left_height, balanced_node.right_height) + 1
        return balanced_node

    def minNode(self, node: AVLNode) -> AVLNode:
        if not node.left_child:
            return node
        else:
            return self.minNode(node.left_child)
