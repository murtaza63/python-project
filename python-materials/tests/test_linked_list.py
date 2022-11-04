#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import unittest
from typing import Optional, TypeVar

from src.linked_list import LinkedList, Node

T = TypeVar("T")


def unwrap(arg: Optional[T]) -> T:
    assert arg is not None
    return arg


class TestLinkedList(unittest.TestCase):
    def test_init_with_array(self) -> None:
        linked_list = LinkedList[int](*[1, 2, 3])  # Must "splat" array
        assert str(linked_list) == "1 -> 2 -> 3 -> None"

    def test_init_with_values(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)
        assert str(linked_list) == "1 -> 2 -> 3 -> None"

    def test_push(self) -> None:
        linked_list = LinkedList[int]()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        assert str(linked_list) == "3 -> 2 -> 1 -> None"

    def test_append(self) -> None:
        linked_list = LinkedList[int]()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        assert str(linked_list) == "1 -> 2 -> 3 -> None"

    def test_node_at_index(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"
        # Item "None" of "Optional[Node[int]]" has no attribute "value"mypy(error)
        assert linked_list.node_at_index(0).value == 1  # type: ignore
        assert linked_list.node_at_index(1).value == 2  # type: ignore
        assert linked_list.node_at_index(2).value == 3  # type: ignore
        assert linked_list.node_at_index(3) is None

    def test_remove_last(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"

        assert linked_list.remove_last() == 3
        assert str(linked_list) == "1 -> 2 -> None"

        assert linked_list.remove_last() == 2
        assert str(linked_list) == "1 -> None"

        assert linked_list.remove_last() == 1
        assert str(linked_list) == "None"

        assert linked_list.remove_last() is None

    def test_pop(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"

        assert linked_list.pop() == 1
        assert str(linked_list) == "2 -> 3 -> None"

        assert linked_list.pop() == 2
        assert str(linked_list) == "3 -> None"

        assert linked_list.pop() == 3
        assert str(linked_list) == "None"

        assert linked_list.pop() is None

    def test_insert_value_after_node(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"

        second_node: Node[int] = unwrap(linked_list.node_at_index(1))
        inserted_node = linked_list.insert_value_after_node(4, second_node)
        assert inserted_node.value == 4
        assert str(linked_list) == "1 -> 2 -> 4 -> 3 -> None"

        linked_list.insert_value_after_node(5, unwrap(linked_list.head))
        assert str(linked_list) == "1 -> 5 -> 2 -> 4 -> 3 -> None"

        linked_list.insert_value_after_node(6, unwrap(linked_list.tail))
        assert str(linked_list) == "1 -> 5 -> 2 -> 4 -> 3 -> 6 -> None"

    def test_remove_after_node(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"
        removed_value = linked_list.remove_after_node(unwrap(linked_list.head))
        assert removed_value == 2
        assert str(linked_list) == "1 -> 3 -> None"

        removed_value = linked_list.remove_after_node(unwrap(linked_list.head))
        assert removed_value == 3
        assert str(linked_list) == "1 -> None"

        removed_value = linked_list.remove_after_node(unwrap(linked_list.head))
        assert removed_value is None
        assert str(linked_list) == "1 -> None"

    def test_iteration(self) -> None:
        linked_list = LinkedList[int](1, 2, 3)  # "1 -> 2 -> 3 -> None"
        values = list(linked_list)
        assert values == [1, 2, 3]


if __name__ == "__main__":
    unittest.main(verbosity=2)
