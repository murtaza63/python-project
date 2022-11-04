#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Optional
from sources.adjacency_list import AdjacencyList
from sources.graph import EdgeType

"""
 # 2. Graph your Friends

 Vincent has three friends, Chesley, Ruiz, and Patrick. Ruiz has friends Ray, Sun, and a mutual friend with Vincent's. Patrick is friends with Cole, and Kerry. Cole is friends with Ruiz and Vincent. Create an adjacency list that represents this friendship graph. Which mutual friend do Ruiz and Vincent Optional[share]
"""

graph = AdjacencyList()

vincent = graph.create_vertex("vincent")
chesley = graph.create_vertex("chesley")
ruiz = graph.create_vertex("ruiz")
patrick = graph.create_vertex("patrick")
ray = graph.create_vertex("ray")
sun = graph.create_vertex("sun")
cole = graph.create_vertex("cole")
kerry = graph.create_vertex("kerry")

graph.add_edge_of_type(EdgeType.UNDIRECTED, vincent, chesley, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, vincent, ruiz, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, vincent, patrick, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, ruiz, ray, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, ruiz, sun, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, patrick, cole, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, patrick, kerry, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, cole, ruiz, 1)
graph.add_edge_of_type(EdgeType.UNDIRECTED, cole, vincent, 1)

print(graph)

print("Ruiz and Vincent both share a friend name Cole")

vincents_friends = set(x.destination.data for x in graph.edges_from_source(vincent))
mutual = vincents_friends.intersection(set(x.destination.data for x in graph.edges_from_source(ruiz)))
print(mutual)
