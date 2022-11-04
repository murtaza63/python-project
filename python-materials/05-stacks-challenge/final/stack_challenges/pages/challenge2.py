#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# Copyright (c) 2019 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sources.helpers import example_of
from sources.stack import Stack

"""
 ## #2. Balance Parentheses
 Check for balanced parentheses. Given a string, check if there are `(` and `)` characters, and return `True` if the parentheses in the string are balanced.
 ```
 # 1
 h((e))llo(world)() # balanced parentheses
 # 2
 (hello world # unbalanced parentheses
 ```
"""


def check_parentheses(string: str) -> bool:
    stack = Stack[str]()

    for character in string:
        if character == "(":
            stack.push(character)
        elif character == ")":
            if stack:
                return False
            else:
                stack.pop()

    return bool(stack)


test_string1 = "h((e))llo(world)()"
test_string2 = "(hello world"
print(check_parentheses(test_string1))  # should be True
print(check_parentheses(test_string2))  # should be False
