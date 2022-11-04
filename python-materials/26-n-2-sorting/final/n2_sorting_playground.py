#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# TODO: Fix imports and make this file run

# import importlib
import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

# n2sorting = importlib.import_module("n2-sorting")
# n2sorting = __import__("n2-sorting")

from n2_sorting.sources.bubble_sort import bubble_sort
from n2_sorting.sources.helpers import example_of
from n2_sorting.sources.insertion_sort import insertion_sort
from n2_sorting.sources.selection_sort import selection_sort

with example_of("bubble sort"):
    array = [9, 4, 10, 3]
    print(f"Original: {array}")
    bubble_sort(array)
    print(f"Bubble sorted: {array}")

with example_of("selection sort"):
    array = [9, 4, 10, 3]
    print(f"Original: {array}")
    selection_sort(array)
    print(f"Selection sorted: {array}")

with example_of("insertion sort"):
    array = [9, 4, 10, 3]
    print(f"Original: {array}")
    insertion_sort(array)
    print(f"Insertion sorted: {array}")
