#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from abc import abstractmethod
from typing import Optional, Protocol, TypeVar

Element = TypeVar("Element")


class Queue(Protocol[Element]):
    @abstractmethod
    def enqueue(self, element: Element) -> bool:
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> Optional[Element]:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def peek(self) -> Optional[Element]:
        raise NotImplementedError
