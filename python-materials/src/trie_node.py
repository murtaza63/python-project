#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from typing import Generic, Optional, TypeVar

Key = TypeVar("Key")


class TrieNode(Generic[Key]):
    def __init__(self, key: Optional[Key], parent: Optional[TrieNode]):
        self.key: Optional[Key] = key
        self.parent: Optional[TrieNode] = parent
        self.children: dict[Key, TrieNode] = {}
        self.is_terminating = False
