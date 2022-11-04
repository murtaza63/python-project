#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from linked_list.sources.helpers import example_of
from linked_list.sources.linked_list import LinkedList, Node

with example_of("creating and linking nodes"):
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)

    node1.next = node2
    node2.next = node3

    print(node1)

with example_of("push"):
    linked_list = LinkedList[int]()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print(list)

with example_of("append"):
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print(linked_list)

with example_of("inserting at a particular index"):
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    print(f"Before inserting: {linked_list}")
    middle_node = linked_list.node_at_index(1)
    assert middle_node is not None
    for _ in range(1, 4 + 1):
        middle_node = linked_list.insert_value_after_node(-1, middle_node)
    print(f"After inserting: {linked_list}")

with example_of("pop"):
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print(f"Before popping list: {linked_list}")
    popped_value = linked_list.pop()
    print(f"After popping list: {linked_list}")
    print("Popped value: " + str(popped_value))

with example_of("removing the last node"):
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print(f"Before removing last node: {linked_list}")
    removed_value = linked_list.pop()

    print(f"After removing last node: {linked_list}")
    print("Removed value: " + str(removed_value))

with example_of("removing a node after a particular node"):
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)

    print(f"Before removing at particular index: {linked_list}")
    index = 1
    node = linked_list.node_at_index(index - 1)
    assert node is not None
    removed_value = linked_list.remove_after_node(node)

    print(f"After removing at index {index}: {linked_list}")
    print("Removed value: " + str(removed_value))

with example_of("using collection"):
    linked_list = LinkedList()
    for i in range(9 + 1):
        linked_list.append(i)

    print(f"List: {linked_list}")
    # TODO: TypeError: 'LinkedList' object is not subscriptable
    # print(f"First element: {list[0]}")
    # print(f"Array containing first 3 elements: {list[0:3]}")
    # print(f"Array containing last 3 elements: {list[-3:]}")

    sum_of_values = sum(linked_list)
    print(f"Sum of all values: {sum_of_values}")

with example_of("array cow"):
    array1 = [1, 2]
    array2 = array1

    print(f"array1: {array1}")
    print(f"array2: {array2}")

    print("---After adding 3 to array 2---")
    array2.append(3)
    print(f"array1: {array1}")
    print(f"array2: {array2}")

with example_of("linked list cow"):
    list1 = LinkedList[int]()
    list1.append(1)
    list1.append(2)
    list2 = list1
    print(f"List1: {list1}")
    print(f"List2: {list2}")

    print("After appending 3 to list2")
    list2.append(3)
    print(f"List1: {list1}")
    print(f"List2: {list2}")

    print("Removing middle node on list2")
    if node := list2.node_at_index(0):
        list2.remove_after_node(node)
    print(f"List2: {list2}")
