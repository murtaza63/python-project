#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: Element, other: Element) -> bool:
        pass


Element = TypeVar("Element", bound=Comparable)
