#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from trie_challenge.sources.helpers import example_of
from trie_challenge.sources.trie import Trie

"""
 ## Challenge 2: Additional properties

 The current implementation of the trie is missing some notable operations. Your task for this challenge is to augment the current implementation of the trie by adding the following:

 1. A `collections` property that returns all the collections in the trie.

 2. A `count` property that tells you how many collections are currently in the trie.

 3. A `is_empty` property that returns `True` if the trie is empty, `False` otherwise.

 Add code to the **Trie.swift** file in the Sources folder.
"""

with example_of("collections"):
    trie = Trie()
    trie.insert("car")
    trie.insert("card")
    trie.insert("care")
    trie.insert("cared")
    trie.insert("cars")
    trie.insert("carbs")
    trie.insert("carapace")
    trie.insert("cargo")

    sorted(trie.collections) == ["car", "carapace", "carbs", "card", "care", "cared", "cargo", "cars"]
    print(trie.collections)
    print(trie.count)  # 8
    print(trie.is_empty)
