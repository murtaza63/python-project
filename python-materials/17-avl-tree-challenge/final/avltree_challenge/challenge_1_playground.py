#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


"""
 # AVL Tree Challenges
 ## Challenge 1
 How many **leaf** nodes are there in a perfectly balanced tree of height 3? What about a perfectly balanced tree of height `h`?
"""


def leaf_nodes_in_tree_of_height(height: int) -> int:
    return int(pow(2.0, float(height)))


answer = leaf_nodes_in_tree_of_height(3)
print(f"Answer: {answer}")
