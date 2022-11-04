#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.graphs.graph import Graph
from sources.graphs.vertex import Vertex
from sources.queue.queue_stack import QueueStack
from sources.graphs.adjacency_list import AdjacencyList
from sources.graphs.graph import EdgeType

"""
 ## 3. Disconnected Graph
 Add a method to `Graph` to detect if a graph is disconnected.

 To help you solve this challenge, a property `all_vertices` was added
 to the `Graph` protocol:

 ```swift
 def all_vertices(self) -> [Vertex]: ...
 ```

 This property is already implemented by `AdjacencyMatrix` and `AdjacencyList`.
"""


def breadth_first_search_from_source(graph: Graph, source: Vertex) -> list[Vertex]:
    queue = QueueStack[Vertex]()
    enqueued = set[Vertex]()
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


def is_disconnected(graph: Graph) -> bool:
    first_vertex = graph.vertices[0] if graph.vertices else None
    if not first_vertex:
        return False
    visited = breadth_first_search_from_source(graph, first_vertex)
    for vertex in graph.vertices:
        if vertex not in visited:
            return True
    return False


#: ![challenge3Sample](challenge3Sample.png)

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
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, h, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, f, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, f, g, None)

print("is_disconnected:", is_disconnected(graph))

# Add the following connection to connect the graphs
graph.add_edge_of_type(EdgeType.UNDIRECTED, a, e, None)
print("is_disconnected:", is_disconnected(graph))
