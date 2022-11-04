#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, TypeVar

T = TypeVar("T")


class Vertex(Generic[T]):
    def __init__(self, index: int, data: T):
        self.index = index
        self.data = data

    def __str__(self) -> str:
        return f"{self.index}: {self.data}"


if __name__ == "__main__":
    vertex = Vertex(index=1, data="hello")
    print(vertex)
