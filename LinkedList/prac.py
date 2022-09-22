

import unittest
import linkedList
list1 = linkedList.LinkedList()
list1.push(11)
def add(x, y):
    return x + y

class SimpleTest(unittest.TestCase):
    def testadd(self):
        self.assertEqual(list(list1.push(12)), [2])

if __name__=='__main__':
    unittest.main()
linkedList.example("push")
list1.push(10)
list1.push(9)
list1.push(8)
list1.push(7)
list1.push(6)

list1.printLL()
