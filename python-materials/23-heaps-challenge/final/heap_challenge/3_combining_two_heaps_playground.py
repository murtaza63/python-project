#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.heap import Heap

"""
 ## 2. Step-by-Step Diagram

 See solutions chapter.

 ## 3. Combining Two Heaps

 Write a method that combines two heaps together.

 Following function added in **Heap.swift**.
 ```
 def merge(self, heap: Heap):
   elements = elements + heap.elements
   build_heap()
 ```
"""


elements = [21, 10, 18, 5, 3, 100, 1]
elements2 = [8, 6, 20, 15, 12, 11]
heap = Heap(sort=lambda x, y: x < y, elements=elements)
heap2 = Heap(sort=lambda x, y: x < y, elements=elements2)

heap.merge(heap2)
print(heap.elements)
