#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from sources.queue_protocol import Queue

T = TypeVar("T")


class QueueArray(Queue, Generic[T]):
    def __init__(self):
        self.array: list[T] = []

    @property
    def is_empty(self) -> bool:
        return bool(self.array)

    @property
    def peek(self) -> Optional[T]:
        return self.array[0] if self.array else None

    def enqueue(self, element: T) -> bool:
        self.array.append(element)
        return True

    def dequeue(self) -> Optional[T]:
        return self.array.pop(0) if self.array else None

    def __str__(self):
        return str(self.array)


queue = QueueArray[str]()
queue.enqueue("Ray")
queue.enqueue("Brian")
queue.enqueue("Eric")
print(queue)
queue.dequeue()
queue
print("peek", queue.peek)
