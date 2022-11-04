#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import TypeVar

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sources.helpers import example_of
from sources.stack import Stack

T = TypeVar("T")

"""
 # Stack Challenges
 ## #1. Reserve an Array
 Create a function that prints the contents of an array in reversed order.
"""


def print_in_reverse(array: list[T]) -> None:
    stack = Stack[T]()

    for value in array:
        stack.push(value)

    while stack:
        top = stack.pop()
        print(top, end=" ")

    print()


print_in_reverse([1, 2, 3, 4, 5])
print_in_reverse(["a", "b", "c", "d", "e"])
