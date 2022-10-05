class QueryArray:
    
    def __init__(self,arr):
        self.arr = arr
    

    def isEmpty(self):
        if len(self.arr) == 0:
            return True 
        else:
             return False
    def enqueue(self,item):
        self.arr.append(item)
        
    def dequeue(self):
        if (len(self.arr ) > 0):
            self.arr.pop(0)
        

    def printQueue(self):
        print(self.arr)
    def peek(self):
        if (len(self.arr) > 0):
            print(self.arr[0])
        else:
            print("Queue is empty so there is no any peek element")



queue = QueryArray()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.enqueue(6)

queue.dequeue()
queue.dequeue()
queue.dequeue()


print(queue.peek())

queue.printQueue()