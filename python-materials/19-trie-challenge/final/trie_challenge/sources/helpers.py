#!/usr/bin/env python

# Copyright (c) 2022 Razeware LLC
# For full license & permission details, see LICENSE.markdown.

# mypy: disallow-untyped-defs

from contextlib import contextmanager
from typing import Generator


@contextmanager
def example_of(text: str) -> Generator:
    print(f"\n---Begin: Example of {text}---")
    try:
        yield
    finally:
        print(f"---End: Example of {text}---")
