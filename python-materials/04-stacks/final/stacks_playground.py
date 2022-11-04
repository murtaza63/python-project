#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from stacks.sources.helpers import example_of
from stacks.sources.stack import Stack

with example_of("using a stack"):
    stack = Stack[int]()  # TODO: mypy doesn't show error if I use Stack[str]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)

    popped_value = stack.pop()
    if popped_value:
        assert popped_value == 4
        print(f"Popped: {popped_value}")

with example_of("initializing a stack from an array literal"):
    float_stack = Stack[float]([1.0, 2.0, 3.0, 4.0])
    print(float_stack)
    float_stack.pop()

with example_of("initializing a stack from an array"):
    array = ["A", "B", "C", "D"]
    str_stack = Stack(array)
    print(str_stack)
    str_stack.pop()
