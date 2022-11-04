#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

import os
import sys
from collections.abc import Callable
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from queue_stack import QueueStack

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.children: list[TreeNode[T]] = []

    def add(self, child: TreeNode) -> None:
        self.children.append(child)

    def for_each_depth_first(self, visit: Callable[[TreeNode], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_depth_first(visit)

    def for_each_level_order(self, visit: Callable[[TreeNode], None]) -> None:
        visit(self)
        queue = QueueStack[TreeNode]()
        for child in self.children:
            queue.enqueue(child)

        while node := queue.dequeue():
            visit(node)
            for child in node.children:
                queue.enqueue(child)

    def search(self, value: T) -> Optional[TreeNode]:
        result: Optional[TreeNode] = None

        def visit(node: TreeNode) -> None:
            if node.value == value:
                result = node

        self.for_each_depth_first(visit)

        return result
