#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


from sources.graph.adjacency_list import AdjacencyList
from sources.graph.dijkstra import Dijkstra
from sources.graph.graph import EdgeType

#:

"""
 ## 2. Find all the shortest paths

 Add a method to class `Dijkstra` that returns a dictionary of all the
 shortest paths to all vertices given a starting vertex.
"""

#: ![challenge1Diagram](challenge1Question.png)

graph = AdjacencyList()

a = graph.create_vertex("A")
b = graph.create_vertex("B")
c = graph.create_vertex("C")
d = graph.create_vertex("D")
e = graph.create_vertex("E")

graph.add_edge_of_type(EdgeType.Directed, a, b, 1)
graph.add_edge_of_type(EdgeType.Directed, a, e, 21)
graph.add_edge_of_type(EdgeType.Directed, a, c, 12)
graph.add_edge_of_type(EdgeType.Directed, b, d, 9)
graph.add_edge_of_type(EdgeType.Directed, b, c, 8)
graph.add_edge_of_type(EdgeType.Directed, d, e, 2)
graph.add_edge_of_type(EdgeType.Directed, c, e, 2)

print(graph)

dijkstra = Dijkstra(graph=graph)
paths_dict = dijkstra.get_all_shortest_paths(a)

for vertex, path in paths_dict.items():
    print(f"Path to {vertex} from {a}")
    for edge in path:
        print(f"{edge.source} --|{edge.weight or 0.0}|--> {edge.destination}")
    print("\n")


"""
ERROR: Compile Failed! Return Code: 1

STDERR:
  File "python-materials-generated/43-dijkstra-shortest-path-challenge/final/dijkstra/pages/2_find_all_the_shortest_paths_playground.py", line 25
    graph.add_edge_of_type(EdgeType.DIRECTED, a, b, 1)
                                              ^
SyntaxError: invalid syntax
"""
