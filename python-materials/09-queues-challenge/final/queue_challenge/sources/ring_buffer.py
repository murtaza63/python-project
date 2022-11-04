#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class RingBuffer(Generic[T]):
    def __init__(self, count: int):
        self.array: list[Optional[T]] = [None for _ in range(count)]
        self.read_index = 0
        self.write_index = 0

    @property
    def first(self) -> Optional[T]:
        return self.array[self.read_index]

    def write(self, element: T) -> bool:
        if not self.is_full:
            self.array[self.write_index % len(self.array)] = element
            self.write_index += 1
            return True
        else:
            return False

    def read(self) -> Optional[T]:
        if not self.is_empty:
            element = self.array[self.read_index % len(self.array)]
            self.read_index += 1
            return element
        else:
            return None

    @property
    def available_space_for_reading(self) -> int:
        return self.write_index - self.read_index

    @property
    def is_empty(self) -> bool:
        return self.available_space_for_reading == 0

    @property
    def available_space_for_writing(self) -> int:
        return len(self.array) - self.available_space_for_reading

    @property
    def is_full(self) -> bool:
        return self.available_space_for_writing == 0

    def __str__(self):
        return str(self.array)
        # values = range(self.available_space_for_reading).map:
        #   str(array[($0 + read_index) % len(array)]!)
        # return "[" + ", ".join(values) + "]"
