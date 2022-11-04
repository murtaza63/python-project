#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from binary_search.sources.binary_search import binary_search_iterative

array = [1, 5, 15, 17, 19, 22, 24, 31, 105, 150]

expected_index = array.index(31)
binary_search_found_index = binary_search_iterative(array, 31)

print(f"Expected Index: {str(expected_index)}")
print(f"Binary Search Index: {str(binary_search_found_index)}")
