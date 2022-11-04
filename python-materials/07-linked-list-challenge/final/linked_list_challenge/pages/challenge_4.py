#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import sys
from typing import Optional

sys.path.insert(0, ".")
from src.helpers import example_of
from src.linked_list import LinkedList

"""
 ## Challenge 4: Merge two lists

 Create a function that takes two sorted linked lists and merges them into a single sorted linked list. Your goal is to return a new linked list that contains the nodes from two lists in sorted order. You may assume the sort order is ascending.
"""


def merge_sorted(left: LinkedList, right: LinkedList) -> LinkedList:
    if left.empty():
        return right
    elif right.empty():
        return left

    # new_head: Optional[Node] = None
    # tail: Node = None  # not optional

    current_left = left.head
    current_right = right.head

    if current_left and current_right:
        if current_left.value < current_right.value:
            new_head = current_left
            current_left = current_left.next
        else:
            new_head = current_right
            current_right = current_right.next
        tail = new_head

    while current_left and current_right:
        if current_left.value < current_right.value:
            tail.next = current_left
            current_left = current_left.next
        else:
            tail.next = current_right
            current_right = current_right.next
        tail = tail.next

    if current_left:
        tail.next = current_left
    elif current_right:
        tail.next = current_right

    linked_list = LinkedList[int]()
    linked_list.head = new_head
    # linked_list.tail =:
    #   while let next = tail.next:
    #     tail = next
    #   return tail
    # }()
    return linked_list


with example_of("merging two lists"):
    linked_list = LinkedList[int](1, 2, 3)
    another_list = LinkedList[int](-3, -2, -1)

    print(f"First list: {linked_list}")
    print(f"Second list: {another_list}")
    merged_list = merge_sorted(linked_list, another_list)
    print(f"Merged list: {merged_list}")
