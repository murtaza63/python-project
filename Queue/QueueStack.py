from typing import Generic, Optional, TypeVar
from Queue import Queue
T = TypeVar("T")
class QueueStack:
    def __init__(self):
        self.leftStack: list[T] = []
        self.rightStack: list[T] = []

    def isEmpty(self)->bool:
        if len(self.leftStack) == 0 and len(self.rightStack) == 0:
            return True 
        else:
            return False 
    def peek(self):
        if len(self.leftStack) != 0:
            return self.leftStack[-1]
        else:
            return self.rightStack
    def enqueue(self, element)-> bool:
        self.rightStack.append(element)
        return True 

    def dequeue(self):
        newStack = [value for value in self.leftStack if value == None]
        if len(self.leftStack) == 0:
            self.leftStack = self.rightStack[::-1]
            newStack
        return self.leftStack.pop(0)
    

queue = QueueStack()
queue.enqueue("Ray")
queue.enqueue("Brian")
print(queue.enqueue(5))
queue.dequeue()
print(queue.peek())