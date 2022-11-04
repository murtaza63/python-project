#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


"""
 ## Challenge 2

 How many **nodes** are there in a perfectly balanced tree of height 3? What about a perfectly balanced tree of height `h`?
"""


def nodes_in_tree_of_height1(height: int) -> int:
    total_height = 0
    for current_height in range(height + 1):
        total_height += int(pow(2.0, float(current_height)))
    return total_height


def nodes_in_tree_of_height2(height: int) -> int:
    return int(pow(2, float(height + 1))) - 1


print(nodes_in_tree_of_height1(3))
print(nodes_in_tree_of_height2(3))
