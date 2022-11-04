#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from general_purpose_tree.sources.helpers import example_of
from general_purpose_tree.sources.tree_node import TreeNode

with example_of("creating a tree"):
    beverages = TreeNode("Beverages")

    hot = TreeNode("Hot")
    cold = TreeNode("Cold")

    beverages.add(hot)
    beverages.add(cold)


def make_beverage_tree() -> TreeNode:
    tree = TreeNode("Beverages")

    hot = TreeNode("hot")
    cold = TreeNode("cold")

    tea = TreeNode("tea")
    coffee = TreeNode("coffee")
    chocolate = TreeNode("cocoa")

    black_tea = TreeNode("black")
    green_tea = TreeNode("green")
    chai_tea = TreeNode("chai")

    soda = TreeNode("soda")
    milk = TreeNode("milk")

    ginger_ale = TreeNode("ginger ale")
    bitter_lemon = TreeNode("bitter lemon")

    tree.add(hot)
    tree.add(cold)

    hot.add(tea)
    hot.add(coffee)
    hot.add(chocolate)

    cold.add(soda)
    cold.add(milk)

    tea.add(black_tea)
    tea.add(green_tea)
    tea.add(chai_tea)

    soda.add(ginger_ale)
    soda.add(bitter_lemon)

    return tree


with example_of("depth-first traversal"):
    tree = make_beverage_tree()
    tree.for_each_depth_first(lambda x: print(x.value))

with example_of("level-order traversal"):
    tree = make_beverage_tree()
    tree.for_each_level_order(lambda x: print(x.value))

with example_of("searching for a node"):
    tree = make_beverage_tree()

    if search_result1 := tree.search("ginger ale"):
        print(f"Found node: {search_result1.value}")

    if search_result2 := tree.search("WKD Blue"):
        print(search_result2.value)
    else:
        print("Couldn't find WKD Blue")
