#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

import os
import sys
from typing import Generic, TypeVar

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from trie_node import TrieNode

Key = TypeVar("Key")


class Trie(Generic[Key]):
    def __init__(self):
        self.root = TrieNode(key=None, parent=None)
        self.collections = set()

    @property
    def count(self) -> int:
        return len(self.collections)

    @property
    def is_empty(self) -> bool:
        return len(self.collections) == 0

    def insert(self, collection: str) -> None:
        current = self.root
        for element in collection:
            if element not in current.children:
                current.children[element] = TrieNode(key=element, parent=current)
            current = current.children[element]
        if current.is_terminating:
            return
        else:
            current.is_terminating = True
            self.collections.add(collection)

    # Support the "in" operator
    def __contains__(self, collection: str) -> bool:
        return self.contains(collection)

    def contains(self, collection: str) -> bool:
        current = self.root
        for element in collection:
            child = current.children[element]
            if not child:
                return False
            current = child
        return current.is_terminating

    def remove(self, collection: str) -> None:
        current = self.root
        for element in collection:
            child = current.children[element]
            if not child:
                return
            current = child
        if not current.is_terminating:
            return
        current.is_terminating = False

        while current.parent and not current.children and not current.is_terminating:
            parent = current.parent
            parent.children.pop(current.key)
            current = parent

    def collections_starting_with_prefix(self, prefix: str) -> list[str]:
        current = self.root
        for element in prefix:
            child = current.children[element]
            if not child:
                return []
            current = child
        return self.collections_starting_with_prefix_after_node(prefix, current)

    def collections_starting_with_prefix_after_node(self, prefix: str, node: TrieNode) -> list[str]:
        # 1
        results: list[str] = []

        if node.is_terminating:
            results.append(prefix)

        # 2
        for child in node.children.values():
            if child.key:
                prefix += child.key
            results.extend(self.collections_starting_with_prefix_after_node(prefix, child))

        return results


if __name__ == "__main__":
    trie: Trie = Trie()
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
