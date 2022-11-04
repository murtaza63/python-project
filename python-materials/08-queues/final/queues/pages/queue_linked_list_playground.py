#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from queue_linked_list.sources.doubly_linked_list import DoublyLinkedList
from sources.queue_protocol import Queue

T = TypeVar("T")


class QueueLinkedList(Queue, Generic[T]):
    def __init__(self):
        self.dll = DoublyLinkedList[T]()

    @property
    def peek(self) -> Optional[T]:
        return self.dll.first if not self.dll.is_empty else None

    @property
    def is_empty(self) -> bool:
        return self.dll.is_empty

    def enqueue(self, element: T) -> bool:
        self.dll.append(element)
        return True

    def dequeue(self) -> Optional[T]:
        if self.dll.is_empty:
            return None
        else:
            element = self.dll.first
            return self.dll.remove(element)

    def __str__(self):
        return str(self.dll)


queue = QueueLinkedList[str]()
queue.enqueue("Ray")
queue.enqueue("Brian")
queue.enqueue("Eric")
queue.dequeue()
print("peek", queue.peek)
