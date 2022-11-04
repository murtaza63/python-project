#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import sys
from typing import Optional

sys.path.insert(0, ".")
from src.helpers import example_of
from src.linked_list import LinkedList, Node

"""
 ## Challenge 2: Find the middle node
 Create a function that finds the middle node of a linked list.
"""


def get_middle(linked_list: LinkedList) -> Optional[Node]:
    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


with example_of("getting the middle node in a list with an odd number of elements"):
    linked_list = LinkedList[int](1, 2, 3)
    print(linked_list)

    middle_node = get_middle(linked_list)
    if middle_node:
        print(middle_node.value)

with example_of("getting the middle node in a list with an even number of elements"):
    linked_list = LinkedList[int](1, 2, 3, 4)
    print(linked_list)

    middle_node = get_middle(linked_list)
    if middle_node:
        print(middle_node.value)
