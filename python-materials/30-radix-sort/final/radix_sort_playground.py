#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# TODO: Make this work

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from radix_sort.sources.helpers import example_of
from radix_sort.sources.radix_sort import radix_sort

with example_of("radix sort"):
    array = [88, 410, 1772, 20]
    print(f"Original array: {array}")
    radix_sort(array)
    print(f"Radix sorted: {array}")
