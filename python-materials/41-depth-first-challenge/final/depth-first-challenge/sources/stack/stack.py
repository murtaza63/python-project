#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# mypy: disallow-untyped-defs

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, elements: list[T] = None):
        self.elements = elements or []

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> Optional[T]:
        return self.elements.pop() if self.elements else None

    def peek(self) -> Optional[T]:
        return self.elements[-1] if self.elements else None

    @property
    def is_empty(self) -> bool:
        return self.peek() is None  # or return bool(self.elements)

    def __bool__(self) -> bool:
        return bool(self.elements)

    def __str__(self) -> str:
        # TODO: Fix Lambda may not be necessaryprospector - pylint(unnecessary-lambda)
        stack_as_str = "\n".join(map(lambda x: str(x), reversed(self.elements)))
        return f"""
----top----
{stack_as_str}
-----------
"""
