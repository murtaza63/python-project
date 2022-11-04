#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# TODO: Get this to work
import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

# TODO: Had to rename merge-sort to merge_sort
from merge_sort.sources.helpers import example_of
from merge_sort.sources.merge_sort import merge_sort

with example_of("merge sort"):
    array = [7, 2, 6, 3, 9]
    print(f"Original: {array}")
    print(f"Merge sorted: {merge_sort(array)}")
