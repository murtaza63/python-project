#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from queue_ring_buffer.sources.ring_buffer import RingBuffer
from sources.queue_protocol import Queue

T = TypeVar("T")


class QueueRingBuffer(Queue, Generic[T]):
    def __init__(self, count: int):
        self.ring_buffer = RingBuffer[T](count=count)

    @property
    def is_empty(self) -> bool:
        return self.ring_buffer.is_empty

    @property
    def peek(self) -> Optional[T]:
        return self.ring_buffer.first if not self.ring_buffer.is_empty else None

    def enqueue(self, element: T) -> bool:
        return self.ring_buffer.write(element)

    def dequeue(self) -> Optional[T]:
        return self.ring_buffer.read()

    def __str__(self):
        return str(self.ring_buffer)


queue = QueueRingBuffer[str](count=10)
queue.enqueue("Ray")
queue.enqueue("Brian")
queue.enqueue("Eric")
queue.dequeue()
print("peek", queue.peek)
