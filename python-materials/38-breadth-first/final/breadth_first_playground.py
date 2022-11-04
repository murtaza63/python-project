#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# TODO: Import from other chapters

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from breadth_first.sources.graphs.adjacency_list import AdjacencyList

# from graph.sources.edge import Edge
# from graph.sources.vertex import Vertex
from breadth_first.sources.graphs.graph import EdgeType, Graph
from breadth_first.sources.graphs.vertex import Vertex
from breadth_first.sources.queue.queue_stack import QueueStack

graph = AdjacencyList()
a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
d = graph.create_vertex("D")
e = graph.create_vertex("E")
f = graph.create_vertex("F")
g = graph.create_vertex("G")
h = graph.create_vertex("H")

graph.add_edge_of_type(EdgeType.UNDIRECTED, a, b, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, a, c, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, a, d, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, b, e, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, c, f, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, c, g, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, h, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, f, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, f, g, None)


def breadth_first_search_from_source(graph: Graph, source: Vertex) -> list[Vertex]:
    queue = QueueStack[Vertex]()
    enqueued: set[Vertex] = set()
    visited: list[Vertex] = []

    queue.enqueue(source)
    enqueued.add(source)

    while vertex := queue.dequeue():
        visited.append(vertex)
        neighbor_edges = graph.edges_from_source(vertex)
        for edge in neighbor_edges:
            if edge.destination not in enqueued:
                queue.enqueue(edge.destination)
                enqueued.add(edge.destination)

    return visited


vertices = breadth_first_search_from_source(graph, a)
for vertex in vertices:
    print(vertex)
