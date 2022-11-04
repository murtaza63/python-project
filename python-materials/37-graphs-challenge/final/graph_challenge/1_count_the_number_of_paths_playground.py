#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.vertex import Vertex
from sources.adjacency_list import AdjacencyList
from sources.graph import EdgeType
from sources.graph import Graph

"""
 # 1. Count the Number of Paths

 Write a method to count the number of paths between two vertices in a directed graph.
"""


def number_of_paths_from_source_to_destination(graph, source: Vertex, destination: Vertex) -> int:
    number_of_paths = 0
    visited: set[Vertex] = set()
    paths_from_source_to_destination(graph, source, destination, visited, number_of_paths)
    return number_of_paths


def paths_from_source_to_destination(graph: Graph, source: Vertex, destination: Vertex, visited: set[Vertex], path_count: int):
    visited.add(source)
    if source == destination:
        path_count += 1
    else:
        neighbors = graph.edges_from_source(source)
        for edge in neighbors:
            if edge.destination not in visited:
                paths_from_source_to_destination(graph, edge.destination, destination, visited, path_count)
    # Remove the vertex from the visited list, so you can find other paths to that node.
    visited.remove(source)


#: ![number_of_paths](number_of_paths.png)

graph = AdjacencyList()

a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
d = graph.create_vertex("D")
e = graph.create_vertex("E")

graph.add_edge_of_type(EdgeType.DIRECTED, a, b, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, a, d, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, a, e, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, a, c, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, b, d, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, b, c, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, d, e, 0)
graph.add_edge_of_type(EdgeType.DIRECTED, c, e, 0)

print(graph)
print(f"Number of {number_of_paths_from_source_to_destination(graph, a, e)}")
