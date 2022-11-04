#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.graph.adjacency_list import AdjacencyList
from sources.graph.vertex import Vertex
from sources.graph.graph import EdgeType

"""
 ## 2. Recursive DFS

 In this chapter we went over an iterative implementation of Depth-first search.
 Now write a recursive implementation.
"""


def depth_first_search_from_start(graph: AdjacencyList, start: Vertex) -> list[Vertex]:
    visited: list[Vertex] = []  # 1
    pushed: set[Vertex] = set()  # 2
    depth_first_search(graph, start, visited, pushed)  # 3
    return visited


def depth_first_search(graph: AdjacencyList, source: Vertex, visited: list[Vertex], pushed: set[Vertex]):
    pushed.add(source)  # 1
    visited.append(source)

    neighbors = graph.edges_from_source(source)
    for edge in neighbors:  # 2
        if edge.destination not in pushed:
            depth_first_search(graph, edge.destination, visited, pushed)  # 3


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
graph.add_edge_of_type(EdgeType.UNDIRECTED, c, g, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, f, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, h, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, f, g, None)
graph.add_edge_of_type(EdgeType.UNDIRECTED, f, c, None)

vertices = depth_first_search_from_start(graph, a)
for vertex in vertices:
    print(vertex)
