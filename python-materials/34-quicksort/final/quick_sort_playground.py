#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# TODO: Fix imports so that this works (without the sys.path.insert)

import os
import sys

# Add current dir to path (TODO: Find a better way to do this)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from quicksort.sources.quicksort_dutch_flag import quicksort_dutch_flag
from quicksort.sources.quicksort_hoare import quicksort_hoare
from quicksort.sources.quicksort_lomuto import quicksort_lomuto
from quicksort.sources.quicksort_median import quicksort_median

list = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
quicksort_lomuto(list, 0, len(list) - 1)
print(list)

list2 = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
quicksort_hoare(list2, 0, len(list2) - 1)
print(list2)

list3 = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
quicksort_median(list3, 0, len(list3) - 1)
print(list3)

list4 = [12, 0, 3, 9, 2, 21, 18, 27, 1, 5, 8, -1, 8]
quicksort_dutch_flag(list4, 0, len(list4) - 1)
print(list4)
