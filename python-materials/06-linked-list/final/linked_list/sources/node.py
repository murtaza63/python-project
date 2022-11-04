#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


from __future__ import annotations

from typing import Generic, Optional, TypeVar

# mypy: disallow-untyped-defs

Value = TypeVar("Value")


class Node(Generic[Value]):
    def __init__(self, value: Value, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if not next:
            return str(self.value)
        return f"{self.value} -> " + str(self.next)


if __name__ == "__main__":
    print("Direct execution of node.py does nothing")
