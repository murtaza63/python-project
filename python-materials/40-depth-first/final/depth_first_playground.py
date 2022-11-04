#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from depth_first.sources.graph.adjacency_list import AdjacencyList
from depth_first.sources.graph.graph import EdgeType, Graph
from depth_first.sources.graph.vertex import Vertex
from depth_first.sources.stack.stack import Stack

# TODO: Import the graph definitions from the 36-graphs chapter

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


def depth_first_search_from_source(graph: Graph, source: Vertex) -> list[Vertex]:
    stack: Stack[Vertex] = Stack()
    pushed: set[Vertex] = set()
    visited: list[Vertex] = []

    stack.push(source)
    pushed.add(source)
    visited.append(source)

    while vertex := stack.peek():
        neighbors = graph.edges_from_source(vertex)
        if not neighbors:
            stack.pop()
            continue
        for edge in neighbors:
            if edge.destination not in pushed:
                stack.push(edge.destination)
                pushed.add(edge.destination)
                visited.append(edge.destination)
                break  # this should do the same thing as continue outer I think
                # continue outer
        stack.pop()

    return visited


if __name__ == "__main__":
    vertices = depth_first_search_from_source(graph, a)
    for vertex in vertices:
        print(vertex)
