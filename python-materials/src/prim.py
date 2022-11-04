#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, Tuple, TypeAlias, TypeVar

T = TypeVar("T")

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from adjacency_list import AdjacencyList
from edge import Edge
from graph import EdgeType
from vertex import Vertex

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from priority_queue.priority_queue import PriorityQueue

# In src dir this is needed
# from priority_queue import PriorityQueue

# from queue import PriorityQueue

Graph: TypeAlias = AdjacencyList


class Prim(Generic[T]):
    def __init__(self):
        pass

    def produce_minimum_spanning_tree(self, graph: Graph) -> Tuple[float, Graph]:
        cost = 0.0
        mst = Graph()
        visited: set[Vertex] = set()

        priority_queue = PriorityQueue[Edge](lambda x, y: x.weight < y.weight, [])

        mst.copy_vertices_from_graph(graph)

        start = graph.vertices[0] if graph.vertices else None
        if not start:
            return (cost, mst)

        visited.add(start)
        self.add_available_edges(start, graph, visited, priority_queue)

        while smallest_edge := priority_queue.dequeue():
            vertex = smallest_edge.destination

            if vertex in visited:
                continue

            visited.add(vertex)
            cost += smallest_edge.weight or 0.0
            mst.add_edge_of_type(EdgeType.UNDIRECTED, smallest_edge.source, smallest_edge.destination, smallest_edge.weight)

            self.add_available_edges(vertex, graph, visited, priority_queue)

        return (cost, mst)

    def add_available_edges(self, vertex: Vertex, graph: Graph, visited: set[Vertex], priority_queue: PriorityQueue[Edge]) -> None:
        for edge in graph.edges_from_source(vertex):
            if edge.destination not in visited:
                priority_queue.enqueue(edge)
