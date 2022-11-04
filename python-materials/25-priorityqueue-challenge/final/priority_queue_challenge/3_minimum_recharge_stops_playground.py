#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.


"""
 ## 3. Minimum Recharge Stops

 Swift-la is a new electric car company that is looking to add a new feature into their vehicles. They want to add the ability for their customers to check if the car can reach a given destination.  Since the journey to the destination may be far, there are charging stations that the car can recharge at. The company wants to find the **minimum number of charging stops** needed for the vehicle to reach its destination.

 You're given the following information:

 - The `target` distance the vehicle needs to travel.
 - The `start_charge`, how much charge the car has to begin the journey.
 - An ordered list of `stations` that the car can potentially stop at to charge along the way.

 Each `ChargingStation` has a `distance` from the start location and a `charge_capacity`. This is the amount of charge a station can add to the car.

 You may assume the following:

 1. An electric car has an **infinite** charge capacity.
 2. One charge capacity is equivalent to one mile.
 3. The list of `stations` is sorted by distance from the start location:

 ```swift
 stations[0].distance < stations[1].distance < stations[k].distance
 ```
"""

from dataclasses import dataclass
from sources.priority_queue import PriorityQueue


@dataclass
class ChargingStation:
    # Distance from start location.
    distance: int
    # The amount of electricity the station has to charge a car.
    # 1 capacity = 1 mile
    charge_capacity: int


# class DestinationResult(Enum):
#   # Able to reach your destination with the minimum number of stops.
#   case reachable(recharge_stops: int)
#   # Unable to reach your destination.
#   case unreachable

# Returns the minimum number of charging stations an electric vehicle needs to reach it's destination.
# - Parameter target: the distance in miles the vehicle needs to travel.
# - Parameter start_charge: the starting charge you have to start the journey.
# - Parameter stations: the charging stations along the way.
def min_recharge_stops_to_target(target: int, start_charge: int, stations: list[ChargingStation]) -> int:
    if start_charge > target:
        return 0

    # Keeps track of the minimum number of stops needed to reach destination
    min_stops = -1
    # Keeps track of the vehicle's current charge on the journey.
    current_charge = 0
    # Tracks the number of stations passed.
    current_station = 0
    # Keeps track of all the station's charge capacity.
    # Responsibility for provide us the station with the highest charging capacity.
    # Initialize the priority queue with the vehicle's starting charge capacity.
    # The priority queue represents all the charging stations that is reachable.
    charge_priority = PriorityQueue(sort=lambda x, y: x > y, elements=[start_charge])

    while not charge_priority.is_empty:
        charge = charge_priority.dequeue()
        if not charge:
            return -1
        current_charge += charge
        min_stops += 1

        if current_charge >= target:
            return min_stops

        while current_station < len(stations) and current_charge >= stations[current_station].distance:
            distance = stations[current_station].charge_capacity
            charge_priority.enqueue(distance)
            current_station += 1
    return -1


# Sample Tests
stations = [
    ChargingStation(distance=10, charge_capacity=60),
    ChargingStation(distance=20, charge_capacity=30),
    ChargingStation(distance=30, charge_capacity=30),
    ChargingStation(distance=60, charge_capacity=40),
]

print(min_recharge_stops_to_target(100, 10, stations))
