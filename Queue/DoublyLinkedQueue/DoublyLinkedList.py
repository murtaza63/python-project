

class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
        self.previous = None
    
class DoublyLinkedList:
    head = None
    tail = None
    first = Node(head)
    def append(self, value):
        newNode = Node(value)
        tailNode = self.tail
        if tailNode == self.tail:
            return tailNode
        else:
            self.head = newNode
            self.tail = newNode
        newNode.previous  = tailNode
        tailNode.next = newNode
        self.tail = newNode

    def remove(self,node:Node):
        prev = node.previous
        next = node.next
        prev = prev
        if prev == prev:
            prev.next = next
        else:
            self.head = self.next
        next.previous = prev
        if self.next == None:
            self.tail = prev

        node.previous = None
        node.next = None
        return node.value
    def makeIterator(self):
        LinkedListIterator(node = self.head)




    
    def printQueue(self):
        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
    
class LinkedListIterator:
    current = Node
    def __init__(self):
        self.current = self.node

    def next(self) -> Node:
        try:
            self.current = self.current.next
        finally:
            return self.current


list3 =  DoublyLinkedList()
list3.append(5)
list3.append(6)

list3.append(7)


list3.printQueue()