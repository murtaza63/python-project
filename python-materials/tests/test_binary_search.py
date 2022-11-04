#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
import unittest

# This only needs to be added to run this file directly as a unit test
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.binary_search import binary_search_in_range, binary_search_iterative, binary_search_recursive


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_iterative(self):
        array = [1, 5, 15, 17, 19, 22, 24, 31, 105, 150]
        found_index = binary_search_iterative(array, 31)
        expected_index = array.index(31)
        assert found_index == expected_index

    def test_binary_search_recursive(self):
        array = [1, 5, 15, 17, 19, 22, 24, 31, 105, 150]
        found_index = binary_search_recursive(array, 31)
        expected_index = array.index(31)
        assert found_index == expected_index

    def test_binary_search_in_range(self):
        array = [1, 5, 15, 17, 19, 22, 24, 31, 105, 150]
        found_index = binary_search_in_range(array, 31)
        expected_index = array.index(31)
        assert found_index == expected_index


if __name__ == "__main__":
    unittest.main()
