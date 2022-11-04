#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

#: ![sample_graph](sample_graph.png)

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from dijkstra_shortest_path.sources.graph.adjacency_list import AdjacencyList
from dijkstra_shortest_path.sources.graph.dijkstra import Dijkstra
from dijkstra_shortest_path.sources.graph.graph import EdgeType

graph = AdjacencyList()

a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
d = graph.create_vertex("D")
e = graph.create_vertex("E")
f = graph.create_vertex("F")
g = graph.create_vertex("G")
h = graph.create_vertex("H")

graph.add_edge_of_type(EdgeType.DIRECTED, a, b, 8)
graph.add_edge_of_type(EdgeType.DIRECTED, a, f, 9)
graph.add_edge_of_type(EdgeType.DIRECTED, a, g, 1)
graph.add_edge_of_type(EdgeType.DIRECTED, b, f, 3)
graph.add_edge_of_type(EdgeType.DIRECTED, b, e, 1)
graph.add_edge_of_type(EdgeType.DIRECTED, f, a, 2)
graph.add_edge_of_type(EdgeType.DIRECTED, h, f, 2)
graph.add_edge_of_type(EdgeType.DIRECTED, h, g, 5)
graph.add_edge_of_type(EdgeType.DIRECTED, g, c, 3)
graph.add_edge_of_type(EdgeType.DIRECTED, c, e, 1)
graph.add_edge_of_type(EdgeType.DIRECTED, c, b, 3)
graph.add_edge_of_type(EdgeType.UNDIRECTED, e, c, 8)
graph.add_edge_of_type(EdgeType.DIRECTED, e, b, 1)
graph.add_edge_of_type(EdgeType.DIRECTED, e, d, 2)

dijkstra = Dijkstra(graph=graph)
paths_from_a = dijkstra.shortest_path_from_start(a)
path = dijkstra.shortest_path_to_destination_with_paths(d, paths_from_a)

for edge in path:
    print(f"{edge.source} --|{edge.weight or 0.0}|--> {edge.destination}")
