#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from trie.sources.helpers import example_of
from trie.sources.trie import Trie

with example_of("insert and contains"):
    trie = Trie()
    trie.insert("cute")
    if "cute" in trie:
        print("cute is in the trie")

with example_of("remove"):
    trie = Trie()
    trie.insert("cut")
    trie.insert("cute")

    print("\n*** Before removing ***")
    assert "cut" in trie
    print('"cut" is in the trie')
    assert "cute" in trie
    print('"cute" is in the trie')

    print("\n*** After removing cut ***")
    trie.remove("cut")
    assert "cut" not in trie
    assert "cute" in trie
    print('"cute" is still in the trie')

with example_of("prefix matching"):
    trie = Trie()
    trie.insert("car")
    trie.insert("card")
    trie.insert("care")
    trie.insert("cared")
    trie.insert("cars")
    trie.insert("carbs")
    trie.insert("carapace")
    trie.insert("cargo")

    print('\n_collections starting with "car"')
    prefixed_with_car = trie.collections_starting_with_prefix("car")
    print(prefixed_with_car)

    print('\n_collections starting with "care"')
    prefixed_with_care = trie.collections_starting_with_prefix("care")
    print(prefixed_with_care)
