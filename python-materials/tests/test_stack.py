#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# mypy: disallow-untyped-defs

import sys
import unittest

from src.stack import Stack

sys.dont_write_bytecode = True  # Don't write *.pyc files


class TestStack(unittest.TestCase):
    def test_initialize_an_empty_stack(self) -> None:
        stack = Stack[int]()  # TODO: mypy doesn't show error if I use Stack[str]()

        with self.subTest(msg="def is_empty"):
            self.assertTrue(stack.is_empty)

        with self.subTest(msg="def __bool__"):
            self.assertFalse(stack)

        with self.subTest(msg="def push()"):
            stack.push(1)
            self.assertFalse(stack.is_empty)
            self.assertTrue(stack)

        with self.subTest(msg="def peek()"):
            self.assertEqual(stack.peek(), 1)
            stack.push(2)
            self.assertEqual(stack.peek(), 2)

        with self.subTest(msg="def pop()"):
            self.assertEqual(stack.pop(), 2)
            self.assertEqual(stack.pop(), 1)
            self.assertIsNone(stack.pop())
            self.assertTrue(stack.is_empty)
            self.assertFalse(stack)

    def test_initialize_a_stack_from_an_int_list(self) -> None:
        stack = Stack([1, 2, 3, 4])
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())

    def test_initialize_a_stack_from_a_str_list(self) -> None:
        stack = Stack(["a", "b", "c", "d"])
        self.assertEqual(stack.pop(), "d")
        self.assertEqual(stack.pop(), "c")
        self.assertEqual(stack.pop(), "b")
        self.assertEqual(stack.pop(), "a")
        self.assertIsNone(stack.pop())


if __name__ == "__main__":
    unittest.main(verbosity=2)
