import Queue
import unittest

class testQueue(unittest.TestCase):
    def test_empty(self):
        myQue = Queue.QueryArray

        self.assertEqual(myQue.isEmpty(self) , True)
        