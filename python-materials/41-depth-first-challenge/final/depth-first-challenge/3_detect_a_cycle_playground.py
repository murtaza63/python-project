#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from sources.graph.adjacency_list import AdjacencyList
from sources.graph.graph import EdgeType
from sources.graph.vertex import Vertex
from sources.graph.graph import Graph

"""
 ## 3. Detect a cycle

 Add a method to `Graph` to detect if a **directed** graph has a cycle.
"""


def has_cycle_from_source(graph: Graph, source: Vertex) -> bool:
    pushed: set[Vertex] = set()
    return has_cycle_from_source_pushed(graph, source, pushed)


def has_cycle_from_source_pushed(graph: Graph, source: Vertex, pushed: set[Vertex]) -> bool:
    pushed.add(source)

    neighbors = graph.edges_from_source(source)
    for edge in neighbors:
        if edge.destination not in pushed and has_cycle_from_source_pushed(graph, edge.destination, pushed):
            return True
        elif edge.destination in pushed:
            return True
    pushed.remove(source)
    return False


#: ![sample_graph2](sample_graph2.png)

graph = AdjacencyList()
a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
d = graph.create_vertex("D")

graph.add_edge_of_type(EdgeType.DIRECTED, a, b, None)
graph.add_edge_of_type(EdgeType.DIRECTED, a, c, None)
graph.add_edge_of_type(EdgeType.DIRECTED, c, a, None)
graph.add_edge_of_type(EdgeType.DIRECTED, b, c, None)
graph.add_edge_of_type(EdgeType.DIRECTED, c, d, None)

print(graph)
print(has_cycle_from_source(graph, a))
