#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    left_stack: list[T] = []
    right_stack: list[T] = []

    def __init__(self):
        self.count = 0

    @property
    def is_empty(self) -> bool:
        return not self.left_stack and not self.right_stack

    @property
    def peek(self) -> Optional[T]:
        if self.left_stack:
            return self.left_stack[-1]
        elif self.right_stack:
            return self.right_stack[0]
        else:
            return None

    def enqueue(self, element: T) -> bool:
        self.count += 1
        self.right_stack.append(element)
        return True

    def dequeue(self) -> Optional[T]:
        if not self.left_stack:
            self.left_stack = list(reversed(self.right_stack))
            self.right_stack.clear()

        value = self.left_stack.pop()
        if value is not None:
            self.count -= 1
        return value
