# #!/usr/bin/env python

# # Copyright (c) 2022 Razeware LLC
# # For full license & permission details, see LICENSE.markdown.

# from typing import Optional


# """
#  # Prim's Algorithm Challenges

#  ## 1. Construct a MST with points

#  Given a set of points, construct a minimum spanning tree connecting the points into a graph.
#  ![Graph](challenge1.png)
# """

# # DOES NOT APPLY TO PYTHON
# import UIKit

# extension CGPoint: Hashable:
#   def hash_into_hasher(self, hasher: Hasher) -> None:
#     hasher.combine(x)
#     hasher.combine(y)

# extension CGPoint:
#   def distance_squared_to_point(self, point: CGPoint) -> CGFloat:
#     x_distance = (x - point.x)
#     y_distance = (y - point.y)
#     return x_distance * x_distance + y_distance * y_distance

#   def distance_to_point(self, point: CGPoint) -> CGFloat:
#     return self.distance_squared_to_point(point).square_root()

# extension Prim where T == CGPoint:
#   def create_complete_graph_with_points(self, points: list[CGPoint]) -> Graph:
#     complete_graph = Graph()

#     # Convert the set of points to vertices
#     points.for_each { point in
#       complete_graph.create_vertex(point)

#     # Create an edge between every vertex, and calculate the distance (weight)
#     # from point to point.
#     complete_graph.vertices.for_each { current_vertex in
#       complete_graph.vertices.for_each { vertex in
#         if current_vertex != vertex:
#           let distance = float(current_vertex.data.distance_to_point(vertex.data))
#           complete_graph.add_directed_edge_from_source_to_destination(current_vertex, vertex, distance)

#     return complete_graph

#   def produce_minimum_spanning_tree_with_points(self, points: list[CGPoint]) -> (cost: float, mst: Graph) -> None:
#     complete_graph = self.create_complete_graph_with_points(points)
#     return self.produce_minimum_spanning_tree(for: complete_graph)

# # Interested in trying out other Optional[points]
# def generate_random_points(count: int, range: Range) -> list[CGPoint]:
#   (len(1..)).map { _ in
#     CGPoint(x=CGFloat.random(in=range), y: CGFloat.random(in: range))

# # You can plot your points using the following:
# # Copy and paste the follow points into `desmos`
# # (4.0, 0.0), (6.0, 16.0), (10.0, 1.0), (3.0, 17.0), (18.0, 7.0), (5.0, 14.0)
# #https:#www.desmos.com//calculator

# points = [CGPoint(x=4, y=0), # 0
#               CGPoint(x=6, y=16), # 1
#               CGPoint(x=10, y=1), # 2
#               CGPoint(x=3, y=17), # 3
#               CGPoint(x=18, y=7), # 4
#               CGPoint(x=5, y=14)] # 5

# (cost, mst) = Prim().produce_minimum_spanning_tree_with_points(points)

# print(mst)
# print(cost)
# #: ### Sample Test Case
# #: ![Table](challenge1_final.png)
