#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from abc import abstractmethod
from enum import Enum
from typing import Optional, Protocol, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from edge import Edge
from vertex import Vertex


class EdgeType(Enum):
    DIRECTED = 1
    UNDIRECTED = 2


Element = TypeVar("Element")


# TODO: Invariant type variable 'Element' used in protocol where contravariant one is expectedmypy(error)
class Graph(Protocol[Element]):
    @abstractmethod
    def create_vertex(self, data: Element) -> Vertex[Element]:
        raise NotImplementedError

    @abstractmethod
    def add_directed_edge(self, source: Vertex[Element], destination: Vertex, weight: Optional[float]) -> None:
        raise NotImplementedError

    @abstractmethod
    def edges_from_source(self, source: Vertex) -> list[Edge]:
        raise NotImplementedError

    @abstractmethod
    def weight_from_source_to_destination(self, source: Vertex, destination: Vertex) -> Optional[float]:
        raise NotImplementedError

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add_edge_of_type(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        if edge.value == EdgeType.DIRECTED.value:
            self.add_directed_edge(source, destination, weight)
        elif edge.value == EdgeType.UNDIRECTED.value:  # edge == EdgeType.UNDIRECTED is returning false for some reason
            self.add_undirected_edge(source, destination, weight)
        else:
            raise Exception

        # TODO: Why does this show a mypy syntax error
        # match edge:
        #     case EdgeType.DIRECTED:
        #         self.add_directed_edge(source, destination, weight)
        #     case EdgeType.UNDIRECTED:
        #         self.add_undirected_edge(source, destination, weight)
