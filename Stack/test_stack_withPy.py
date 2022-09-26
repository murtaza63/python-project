import stack

import pytest


class TestClass:
    s = stack.Stack()
    newStack = s.stackData()
    def test_empty(self):
        assert self.s.checkEmpty(self.newStack) == True

    def test_checkSize(self):
        self.s.push(self.newStack,4)
        self.s.push(self.newStack,3)
        assert self.s.checkSize(self.newStack) == 1
    def test_needsfiles(tmp_path):
        print(tmp_path)
        assert 0
    