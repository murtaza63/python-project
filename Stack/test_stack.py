import unittest
import stack

class StackTester(unittest.TestCase):
    def test_stack_init(self):
        s = stack.Stack()
        newStack = s.stackData()
        s.push(newStack,2)
        self.assertEqual(newStack, [2])
    def test_removeStack(self):
        s = stack.Stack()
        newStack = s.stackData()

        s.push(newStack,4)
        s.push(newStack,3)
        s.push(newStack,2)
        s.push(newStack,1)




        
        self.assertEqual(s.remove(newStack), 1)

    def checkEmpty(self):
        s = stack.Stack()
        newStack = s.stackData()

        self.assertEquals(s.checkEmpty(), True)

if __name__ == "__main__":
    unittest.main()