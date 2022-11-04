#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from typing import Generic, Optional, TypeAlias, TypeVar

T = TypeVar("T")

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from ..priority_queue.priority_queue import PriorityQueue

# from queue import PriorityQueue

from adjacency_list import AdjacencyList
from edge import Edge
from vertex import Vertex

Graph: TypeAlias = AdjacencyList


class Dijkstra(Generic[T]):
    def __init__(self, graph: Graph):
        self.graph = graph

    def route_to_destination_with_paths(self, destination: Vertex, paths: dict[Vertex, Edge]) -> list[Edge]:
        vertex = destination
        path: list[Edge] = []

        while vertex in paths:
            edge = paths[vertex]
            path = [edge] + path
            vertex = edge.source
        return path

    def distance_to_destination_with_paths(self, destination: Vertex, paths: dict[Vertex, Edge]) -> float:
        path = self.route_to_destination_with_paths(destination, paths)
        distances = [x.weight for x in path if x.weight is not None]
        return sum(distances)

    def shortest_path_from_start(self, start_vertex: Vertex) -> dict[Vertex, Edge]:
        paths: dict[Vertex, Edge] = dict()

        priority_queue = PriorityQueue(
            sort=lambda x, y: self.distance_to_destination_with_paths(x, paths) < self.distance_to_destination_with_paths(y, paths), elements=[]
        )
        priority_queue.enqueue(start_vertex)

        while vertex := priority_queue.dequeue():
            for edge in self.graph.edges_from_source(vertex):
                weight = edge.weight
                if not weight:
                    continue
                if (
                    edge.destination != start_vertex
                    and edge.destination not in paths
                    or self.distance_to_destination_with_paths(vertex, paths) + weight < self.distance_to_destination_with_paths(edge.destination, paths)
                ):
                    paths[edge.destination] = edge
                    priority_queue.enqueue(edge.destination)

        return paths

    def shortest_path_to_destination_with_paths(self, destination: Vertex, paths: dict[Vertex, Edge]) -> list[Edge]:
        return self.route_to_destination_with_paths(destination, paths)

    # get_all_shortest_path was only in 43 and not 42
    # 42-dijkstra-shortest-path//projects////dijkstra.playground//Sources//Graph//Dijkstra.swift
    # 43-dijkstra-shortest-path-challenge//projects////dijkstra.playground//Sources//Graph//Dijkstra.swift

    def get_all_shortest_paths(self, source: Vertex) -> dict[Vertex, list[Edge]]:
        paths_dict = dict[Vertex, list[Edge]]()
        paths_from_source = self.shortest_path_from_start(source)
        for vertex in self.graph.vertices:
            path = self.shortest_path_to_destination_with_paths(vertex, paths_from_source)
            paths_dict[vertex] = path
        return paths_dict
