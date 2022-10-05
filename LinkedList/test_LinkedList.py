

import unittest
import linkedList
list1 = linkedList.LinkedList()



class SimpleTest(unittest.TestCase):
    def test_push(self):
        list1.push(4)
        list1.push(3)
        self.assertEqual(list1.printLL(), 3)

    def test_append(self):
        list1.append(3)
        list1.append(4)
        self.assertEqual(list1.printLL(),3)

if __name__=='__main__':
    unittest.main()



