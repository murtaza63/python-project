#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


import unittest

from src.node import Node

# mypy: disallow-untyped-defs


class TestNode(unittest.TestCase):
    def test_creating_and_linking_nodes(self) -> None:
        node1 = Node(value=1)
        node2 = Node(value=2)
        node3 = Node(3)

        node1.next = node2
        node2.next = node3

        self.assertEqual(str(node1), "1 -> 2 -> 3 -> None")


if __name__ == "__main__":
    unittest.main(verbosity=2)
