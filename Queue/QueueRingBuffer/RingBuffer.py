from array import array
from multiprocessing.dummy import Array
from xml.dom.minidom import Element


class RingBuffer:
    array= []
    readIndex = 0
    writeIndex = 0

    def __init__(self,count):
        array = Array()

    def first(self):
        self.array[self.readIndex]
    
    def write(self , element) -> bool:
        if self.isFull() == False:
            self.array[self.writeIndex % len(self.array)] = element
            self.writeIndex += 1
            return True 
        else:
            return False 

    def read(self):
        if self.isEmpty() == False :
            element = self.array[self.readIndex % len(self.array)]
            self.readIndex += 1 
            return element
        else:
            return None

    def availableSpaceForReading(self) -> int:
        self.writeIndex - self.readIndex

    def isEmpty(self)->bool:
        if self.availableSpaceForReading() == 0:
            return True 
        else:
            return False 
    def availableSpaceForWriting(self)->int:
        len(self.array) - self.availableSpaceForReading
    
    def isFull(self)->bool:
        if self.availableSpaceForWriting == 0:
            return True 
        else:
            return False 
            
