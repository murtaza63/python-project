#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from collections.abc import Callable
from typing import Optional, TypeVar

from sources.binary_node import BinaryNode

T = TypeVar("T")

"""
 ## #2. Serialization

 A common task in software development is serializing an object into another
 data type. This process is known as serialization, and allows custom types to
 be used in systems that only support a closed set of data types.

 An example of serialization is JSON. Your task is to devise a way to serialize
 a binary tree into an array, and a way to deserialize the array back into
 the same binary tree.

 To clarify this problem, consider the following binary tree:

 ![Binary Tree](binary-tree.png)

 A particular algorithm may output the serialization as
 `[15, 10, 5, None, None, 12, None, None, 25, 17, None, None, None]`.
 The deserialization process should transform the array back into the same
 binary tree. Note that there are many ways to perform serialization.
 You may choose any way you wish.
"""

root = BinaryNode(value=15)
ten = BinaryNode(value=10)
five = BinaryNode(value=5)
twelve = BinaryNode(value=12)
twenty_five = BinaryNode(value=25)
seventeen = BinaryNode(value=17)

root.left_child = ten
root.right_child = twenty_five
ten.left_child = five
ten.right_child = twelve
twenty_five.left_child = seventeen

tree = root

print(tree)


def traverse_pre_order(node: BinaryNode, visit: Callable[[Optional[T]], None]) -> None:
    visit(node.value)
    if node.left_child:
        traverse_pre_order(node.left_child, visit)
    else:
        print("appending none")
        visit(None)

    if node.right_child:
        traverse_pre_order(node.right_child, visit)
    else:
        print("appending none")
        visit(None)


def serialize(node: BinaryNode) -> list[Optional[T]]:
    array: list[Optional[T]] = []
    node.traverse_pre_order(lambda x: array.append(x))
    return array


def deserialize(array: list[Optional[T]]) -> Optional[BinaryNode]:
    if not array:
        return None

    value = array.pop(0)
    node = BinaryNode(value=value)
    node.left_child = deserialize(array)
    node.right_child = deserialize(array)
    return node


array = serialize(tree)
print(array)
deserialized_tree = deserialize(array)
print(deserialized_tree)

# TODO Fix Bug: This does not work correctly
# assert str(tree) == str(deserialized_tree)
