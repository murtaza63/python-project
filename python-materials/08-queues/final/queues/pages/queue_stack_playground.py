#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from sources.queue_protocol import Queue

T = TypeVar("T")


class QueueStack(Queue, Generic[T]):
    def __init__(self):
        self.left_stack: list[T] = []
        self.right_stack: list[T] = []

    @property
    def is_empty(self) -> bool:
        return bool(self.left_stack) and bool(self.right_stack)

    @property
    def peek(self) -> Optional[T]:
        return self.left_stack[-1] if self.left_stack else self.right_stack[0]

    def enqueue(self, element: T) -> bool:
        self.right_stack.append(element)
        return True

    def dequeue(self) -> Optional[T]:
        if not self.left_stack:
            self.left_stack = list(reversed(self.right_stack))
            self.right_stack.clear()
        return self.left_stack.pop()

    def __str__(self):
        return str(self.left_stack.reversed() + self.right_stack)


queue = QueueStack[str]()
queue.enqueue("Ray")
queue.enqueue("Brian")
queue.enqueue("Eric")
queue.dequeue()
print("peek", queue.peek)
