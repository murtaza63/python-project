#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import sys
from typing import Optional

# Must run with full path for now
# python 07-linked-list-challenge/projects/finished/linked_list_challenge/pages/challenge_1.py
sys.path.insert(0, ".")
from src.helpers import example_of
from src.linked_list import LinkedList, Node

"""
 # Linked List Challenges
 ## Challenge 1: Print in reverse

 Create a function that prints the nodes of a linked list in reverse order.
"""


def print_in_reverse_with_list(linked_list: LinkedList) -> None:
    print_in_reverse_with_node(linked_list.head)


def print_in_reverse_with_node(node: Optional[Node]) -> None:
    if not node:
        return
    print_in_reverse_with_node(node.next)
    print(node.value)


with example_of("printing in reverse"):
    linked_list = LinkedList[int](1, 2, 3)

    print(f"Original list: {linked_list}")
    print("Printing in reverse:")
    print_in_reverse_with_list(linked_list)
