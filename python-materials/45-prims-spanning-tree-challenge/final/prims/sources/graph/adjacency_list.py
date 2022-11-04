#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

import os
import sys
from collections import defaultdict
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from edge import Edge
from graph import Graph
from vertex import Vertex

T = TypeVar("T")


class AdjacencyList(Graph, Generic[T]):
    def __init__(self):
        self.adjacencies: dict[Vertex, list[Edge]] = defaultdict(list[Edge])

    # Only in Ch 42, 43, 44, 45
    @property
    def vertices(self) -> list[Vertex]:
        return list(self.adjacencies.keys())

    def create_vertex(self, data: T) -> Vertex:
        vertex = Vertex(index=len(self.adjacencies), data=data)
        self.adjacencies[vertex] = []
        return vertex

    # Only in Ch 44, 45
    def copy_vertices_from_graph(self, graph: AdjacencyList) -> None:
        for vertex in graph.vertices:
            self.adjacencies[vertex] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        edge = Edge(source=source, destination=destination, weight=weight)
        self.adjacencies[source].append(edge)

    def edges_from_source(self, source: Vertex) -> list[Edge]:
        return self.adjacencies[source] or []

    def weight_from_source_to_destination(self, source: Vertex, destination: Vertex) -> Optional[float]:
        return next(x for x in self.edges_from_source(source) if x.destination == destination).weight

    def __str__(self) -> str:
        result = ""
        for vertex, edges in self.adjacencies.items():
            edge_string = ""
            for index, edge in enumerate(edges):
                if index != len(edges) - 1:
                    edge_string += f"{edge.destination}, "
                else:
                    edge_string += str(edge.destination)
            result += f"{vertex} ---> [ {edge_string} ]\n"
        return result
