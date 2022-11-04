#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from prims_spanning_tree.sources.graph.adjacency_list import AdjacencyList
from prims_spanning_tree.sources.graph.graph import EdgeType
from prims_spanning_tree.sources.graph.prim import Prim

graph = AdjacencyList()
one = graph.create_vertex(1)
two = graph.create_vertex(2)
three = graph.create_vertex(3)
four = graph.create_vertex(4)
five = graph.create_vertex(5)
six = graph.create_vertex(6)

graph.add_edge_of_type(EdgeType.UNDIRECTED, one, two, 6)
graph.add_edge_of_type(EdgeType.UNDIRECTED, one, three, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, one, four, 5)
graph.add_edge_of_type(EdgeType.UNDIRECTED, two, three, 5)
graph.add_edge_of_type(EdgeType.UNDIRECTED, two, five, 3)
graph.add_edge_of_type(EdgeType.UNDIRECTED, three, four, 5)
graph.add_edge_of_type(EdgeType.UNDIRECTED, three, five, 6)
graph.add_edge_of_type(EdgeType.UNDIRECTED, three, six, 4)
graph.add_edge_of_type(EdgeType.UNDIRECTED, four, six, 2)
graph.add_edge_of_type(EdgeType.UNDIRECTED, five, six, 6)

(cost, mst) = Prim().produce_minimum_spanning_tree(graph)
print(f"cost: {cost}")
print("mst:")
print(mst)
