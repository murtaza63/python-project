import Queue
import unittest


class testQueue(unittest.TestCase):
    def test_empty(self):
        arr = []
        myQue = Queue.QueueArray(arr)

        self.assertEqual(myQue.isEmpty() , True)
        

    def test_enqueue(self):
         arr = []
         
         myQue = Queue.QueueArray(arr)
         myQue.enqueue(2)
         self.assertEqual(arr, [2])
        
    def test_dequeue(self):
        arr = [1,2,3,4]
        myQue = Queue.QueueArray(arr)
        element = myQue.dequeue()
        self.assertEqual(element,1)

    def test_FirstElement(self):
        arr = [1,2,3,4]
        myQue = Queue.QueueArray(arr)
        item = myQue.peek()
        self.assertEqual(item, arr[0])


if __name__ == '__main__':
    unittest.main