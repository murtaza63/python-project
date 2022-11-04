#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic

enum Visit<T: Hashable>:
  case start
  case edge(Edge)

class Dijkstra(Generic[T: Hashable]):
  typealias Graph = AdjacencyList
  graph: Graph

  def __init__(self, graph: Graph):
    self.graph = graph

  def route_to_destination_with_paths(self, destination: Vertex, paths: [Vertex: Visit]) -> list[Edge]:
    vertex = destination
    path: [Edge] = []

    while visit := paths[vertex], case let .edge(edge) = visit:
      path = [edge] + path
      vertex = edge.source
    return path

  def distance_to_destination_with_paths(self, destination: Vertex, paths: [Vertex: Visit]) -> float:
    path = self.route_to_destination_with_paths(destination, paths)
    distances = path.compact_map { $0.weight }
    return distances.reduce(0.0, +)

  def shortest_path_from_start(self, start: Vertex) -> [Vertex: Visit]:
    paths: [Vertex: Visit] = [start: .start]

    priority_queue = PriorityQueue<Vertex>(sort::
      self.distance_to_destination_with_paths($0, paths) < self.distance_to_destination_with_paths($1, paths)
    })
    priority_queue.enqueue(start)

    while vertex := priority_queue.dequeue():
      for edge in self.graph.edges_from_source(vertex):
        weight = edge.weight
        if not weight:
          continue
        if paths[edge.destination] is None or self.distance_to_destination_with_paths(vertex, paths) + weight < self.distance_to_destination_with_paths(edge.destination, paths):
          paths[edge.destination] = .edge(edge)
          priority_queue.enqueue(edge.destination)

    return paths

  def shortest_path_to_destination_with_paths(self, destination: Vertex, paths: [Vertex: Visit]) -> list[Edge]:
    return self.route_to_destination_with_paths(destination, paths)

  //** get_all_shortest_path was only in 43 and not 42
   42-dijkstra-shortest-path//projects////dijkstra.playground//Sources//Graph//Dijkstra.swift
   43-dijkstra-shortest-path-challenge//projects////dijkstra.playground//Sources//Graph//Dijkstra.swift
"""

  def get_all_shortest_paths(self, source: Vertex) -> [Vertex: [Edge]]:
    paths_dict = [Vertex: [Edge]]()
    paths_from_source = self.shortest_path_from_start(source)
    for vertex in self.graph.vertices:
      let path = self.shortest_path_to_destination_with_paths(vertex, paths_from_source)
      paths_dict[vertex] = path
    return paths_dict


"""
ERROR: Compile Failed! Return Code: 1

STDERR:
  File "python-materials-generated/43-dijkstra-shortest-path-challenge/final/dijkstra/sources/graph/dijkstra.py", line 30
    distances = path.compact_map { $0.weight }
                                     ^
SyntaxError: invalid decimal literal
"""
