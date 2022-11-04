#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.graphs.graph import Graph
from sources.graphs.vertex import Vertex
from sources.queue.queue_stack import QueueStack
from sources.graphs.adjacency_list import AdjacencyList
from sources.graphs.graph import EdgeType

"""
 ## 2. Iterative BFS

 In this chapter we went over an iterative implementation of breadth-first
 search. Now write a recursive implementation.
"""


def bfs_from_source(graph: Graph, source: Vertex) -> list[Vertex]:
    queue = QueueStack[Vertex]()
    enqueued: set[Vertex] = set()
    visited: list[Vertex] = []

    queue.enqueue(source)
    enqueued.add(source)

    bfs(graph, queue, enqueued, visited)
    return visited


def bfs(graph: Graph, queue: QueueStack[Vertex], enqueued: set[Vertex], visited: list[Vertex]) -> None:
    vertex = queue.dequeue()
    if not vertex:
        return
    visited.append(vertex)
    neighbor_edges = graph.edges_from_source(vertex)
    for edge in neighbor_edges:
        if edge.destination not in enqueued:
            queue.enqueue(edge.destination)
            enqueued.add(edge.destination)
    bfs(graph, queue, enqueued, visited)


#: ![sample_graph](sample_graph.png)

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

print(graph)

vertices = bfs_from_source(graph, a)
for vertex in vertices:
    print(vertex)
