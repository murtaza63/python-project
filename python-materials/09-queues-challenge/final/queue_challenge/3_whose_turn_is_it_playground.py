#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional, Protocol, TypeVar


"""
 # Queue Data Structure Challenges

 ## Challenge 1 & 2

 See solutions chapter.

 ## 3. Whose turn is it?

 Imagine that you are playing a game of Monopoly with your friends. The problem
 is that everyone always forget whose turn it is Create a Monopoly organizer
 that always tells you whose turn it is. Below is a protocol that you can
 conform to:
"""

Player = TypeVar("Player")

from sources.queue_array import QueueArray

# class BoardGameManager(Protocol[Player]):
#     def next_player(self) -> Optional[Player]:


def next_player(queue: QueueArray) -> Optional[Player]:
    person = queue.dequeue()
    if not person:
        return None
    queue.enqueue(person)
    return person


queue = QueueArray()
queue.enqueue("Vincent")
queue.enqueue("Remel")
queue.enqueue("Lukiih")
queue.enqueue("Allison")
print(queue)

print("===== boardgame =======")
next_player(queue)
print(queue)
next_player(queue)
print(queue)
next_player(queue)
print(queue)
next_player(queue)
print(queue)
next_player(queue)
print(queue)
next_player(queue)
print(queue)
