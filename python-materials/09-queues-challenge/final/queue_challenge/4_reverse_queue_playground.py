#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

"""
 ## 4. Reverse Queue

 Implement a method to reverse the contents of a queue.

 > Hint: The `Stack` data structure has been included in the **Sources** folder.
"""

from sources.queue_array import QueueArray
from sources.stack import Stack


def reversed(queue: QueueArray) -> QueueArray:
    stack = Stack()
    while element := queue.dequeue():
        stack.push(element)
    while element := stack.pop():
        queue.enqueue(element)
    return queue


queue = QueueArray()
queue.enqueue("1")
queue.enqueue("21")
queue.enqueue("18")
queue.enqueue("42")

print(f"before: {queue}")
print(f"after: {reversed(queue)}")
