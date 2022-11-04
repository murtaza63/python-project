#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from graphs.sources.adjacency_matrix import AdjacencyMatrix
from graphs.sources.graph import EdgeType

graph = AdjacencyMatrix()

singapore = graph.create_vertex("Singapore")
tokyo = graph.create_vertex("Tokyo")
hong_kong = graph.create_vertex("Hong Kong")
detroit = graph.create_vertex("Detroit")
san_francisco = graph.create_vertex("San Francisco")
washington_d_c = graph.create_vertex("Washington DC")
austin_texas = graph.create_vertex("Austin Texas")
seattle = graph.create_vertex("Seattle")

graph.add_edge_of_type(EdgeType.UNDIRECTED, singapore, hong_kong, 300)
graph.add_edge_of_type(EdgeType.UNDIRECTED, singapore, tokyo, 500)
graph.add_edge_of_type(EdgeType.UNDIRECTED, hong_kong, tokyo, 250)
graph.add_edge_of_type(EdgeType.UNDIRECTED, tokyo, detroit, 450)
graph.add_edge_of_type(EdgeType.UNDIRECTED, tokyo, washington_d_c, 300)
graph.add_edge_of_type(EdgeType.UNDIRECTED, hong_kong, san_francisco, 600)
graph.add_edge_of_type(EdgeType.UNDIRECTED, detroit, austin_texas, 50)
graph.add_edge_of_type(EdgeType.UNDIRECTED, austin_texas, washington_d_c, 292)
graph.add_edge_of_type(EdgeType.UNDIRECTED, san_francisco, washington_d_c, 337)
graph.add_edge_of_type(EdgeType.UNDIRECTED, washington_d_c, seattle, 277)
graph.add_edge_of_type(EdgeType.UNDIRECTED, san_francisco, seattle, 218)
graph.add_edge_of_type(EdgeType.UNDIRECTED, austin_texas, san_francisco, 297)

graph.weight_from_source_to_destination(singapore, tokyo)

print("San Francisco Outgoing Flights:")
print("--------------------------------")
for edge in graph.edges_from_source(san_francisco):
    print(f"from: {edge.source} to: {edge.destination}")
