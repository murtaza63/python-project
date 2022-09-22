import unittest
import stack

class StackTester(unittest.TestCase):
    def test_stack_init(self):
        s = stack.Stack()
        self.assertEqual(0, s.size())