#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from general_tree_challenge.sources.tree_node import TreeNode
from general_tree_challenge.sources.queue_with_count import Queue

#: # #1. Print a Tree in Level Order
#:
#: Print all the values in a tree in an order based on their level.
#: Nodes in the same level should be printed on the same line.
#: For example, consider the following tree:
#:
#: ![Image of Tree](tree.png)
#:
#: Your algorithm should prinnt the following:
#:
#: ```none
#: 15
#: 1 17 20
#: 1 5 0 2 5 7
#: ```
#:
#: **Hint**: Consider using a `Queue` included for you in **Sources**.
# Build the sample tree shown in the diagram
# Root of the tree

tree = TreeNode(15)

# Second level
one = TreeNode(1)
tree.add(one)

seventeen = TreeNode(17)
tree.add(seventeen)

twenty = TreeNode(20)
tree.add(twenty)

# Third level
one2 = TreeNode(1)
five = TreeNode(5)
zero = TreeNode(0)
one.add(one2)
one.add(five)
one.add(zero)

two = TreeNode(2)
seventeen.add(two)

five2 = TreeNode(5)
seven = TreeNode(7)
twenty.add(five2)
twenty.add(seven)

# Solution


def print_each_level_for_tree(tree: TreeNode) -> None:
    queue = Queue[TreeNode]()
    nodes_left_in_current_level = 0

    queue.enqueue(tree)
    while not queue.is_empty:
        nodes_left_in_current_level = queue.count
        while nodes_left_in_current_level > 0:
            node = queue.dequeue()
            if not node:
                break
            print(f"{node.value} ", end="")
            for child in node.children:
                queue.enqueue(child)
            nodes_left_in_current_level -= 1
        print()


print_each_level_for_tree(tree)
