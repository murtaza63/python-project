#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional

#: ## Challenge 2: Find a duplicate
#: Given a collection of Equatable elements, return the first element
#: that is a duplicate in the collection.


def first_duplicate(array: list[int]) -> Optional[int]:
    found = set()
    for value in array:
        if value in found:
            return value
        else:
            found.add(value)
    return None


array = [2, 4, 5, 5, 2]
print(first_duplicate(array))
