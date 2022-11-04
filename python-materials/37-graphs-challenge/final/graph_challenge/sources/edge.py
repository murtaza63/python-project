#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, TypeVar

from vertex import Vertex

T = TypeVar("T")


class Edge(Generic[T]):
    def __init__(self, source: Vertex[T], destination: Vertex[T], weight: Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self) -> str:
        return f"({self.source}) --{self.weight}--> ({self.destination})"


if __name__ == "__main__":
    source_vertex = Vertex[str](index=0, data="Zero")
    dest_vertex = Vertex[str](index=1, data="One")
    edge = Edge[str](source_vertex, dest_vertex, 10)
    print(edge)
