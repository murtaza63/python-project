#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from dataclasses import dataclass
from sources.priority_queue import PriorityQueue

"""
 ## 2. Prioritize a Waitlist

 Your favorite T-Swift concert was sold out. Fortunately there is a waitlist for people who still want to go However the ticket sales will first prioritize someone with a **military background**, followed by **seniority**. Write a `sort` function that will return the list of people on the waitlist by the priority mentioned.
"""


@dataclass
class Person:
    name: str
    age: int
    is_military: bool


def tswift_sort(person1: Person, person2: Person) -> bool:
    if person1.is_military == person2.is_military:
        return person1.age > person2.age

    return person1.is_military


p = Person(name="Josh", age=21, is_military=True)
p2 = Person(name="Jake", age=22, is_military=True)
p3 = Person(name="Clay", age=28, is_military=False)
p4 = Person(name="Cindy", age=28, is_military=False)
p5 = Person(name="Sabrina", age=30, is_military=False)

waitlist = [p, p2, p3, p4, p5]

priority_queue = PriorityQueue(sort=tswift_sort, elements=waitlist)
while not priority_queue.is_empty:
    print(priority_queue.dequeue())
