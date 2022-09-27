

import unittest
import linkedList
list1 = linkedList.LinkedList()
list1.push(11)


class SimpleTest(unittest.TestCase):
    def test_add(self):
        list1.push(4)
        self.assertEqual(list1.printLL(), [2])

if __name__=='__main__':
    unittest.main()
linkedList.example("push")
list1.push(10)
list1.push(9)
list1.push(8)
list1.push(7)
list1.push(6)

list1.printLL()


