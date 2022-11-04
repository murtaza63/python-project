#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys
from typing import Generic, Optional, TypeVar

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from edge import Edge
from graph import Graph
from vertex import Vertex

T = TypeVar("T")


class AdjacencyMatrix(Graph, Generic[T]):
    def __init__(self):
        self.vertices: list[Vertex] = []
        self.weights: list[list[Optional[float]]] = []

    def create_vertex(self, data: T) -> Vertex:
        vertex = Vertex(index=len(self.vertices), data=data)
        self.vertices.append(vertex)
        for i in range(len(self.weights)):
            self.weights[i].append(None)
        row: list[Optional[float]] = [None] * len(self.vertices)
        self.weights.append(row)
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.weights[source.index][destination.index] = weight

    def edges_from_source(self, source: Vertex) -> list[Edge]:
        edges: list[Edge] = []
        for column in range(len(self.weights)):
            if column in self.weights[source.index]:
                weight = self.weights[source.index][column]
                edges.append(Edge(source=source, destination=self.vertices[column], weight=weight))
        return edges

    def weight_from_source_to_destination(self, source: Vertex, destination: Vertex) -> Optional[float]:
        return self.weights[source.index][destination.index]

    def __str__(self) -> str:
        # 1
        vertices_description = "\n".join([str(x) for x in self.vertices])
        # 2
        grid: list[str] = []
        for i in range(len(self.weights)):
            row = ""
            for j in range(len(self.weights)):
                if value := self.weights[i][j]:
                    row += f"{value}\t"
                else:
                    row += "ø\t\t"
            grid.append(row)
        edges_description = "\n".join(grid)
        # 3
        return f"{vertices_description}\n\n{edges_description}"
