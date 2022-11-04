#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# This is needed when a type is used in itself
from __future__ import annotations

from collections.abc import Callable
from typing import Generic, Optional, TypeVar

Element = TypeVar("Element")


class BinaryNode(Generic[Element]):
    def __init__(self, value: Element):
        self.value = value
        self.left_child: Optional[BinaryNode[Element]] = None
        self.right_child: Optional[BinaryNode[Element]] = None

    def __str__(self) -> str:
        return self.diagram_for_node(self)

    def diagram_for_node(self, node: Optional[BinaryNode], top: str = "", root: str = "", bottom: str = "") -> str:
        if not node:
            return root + "None\n"

        if node.left_child is None and node.right_child is None:
            return root + f"{node.value}\n"

        return (
            self.diagram_for_node(node.right_child, top + " ", top + "┌──", top + "│ ")
            + root
            + f"{node.value}\n"
            + self.diagram_for_node(node.left_child, bottom + "│ ", bottom + "└──", bottom + " ")
        )

    def traverse_in_order(self, visit: Callable[[Element], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self.value)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Element], None]) -> None:
        visit(self.value)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Element], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self.value)
