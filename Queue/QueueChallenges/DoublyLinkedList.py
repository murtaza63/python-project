


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        if self.head == None:
            return True 
        else:
            return False
        first = self.head
        last = self.tail
    def prepend(self, value):
        newNode = Node(value)
        headNode = self.head
        if headNode:
            return headNode
        else:
            self.head = newNode
            self.tail = newNode
            return  
        newNode.prev = None
        newNode.next = headNode
        headNode.prev = newNode
        self.head = newNode

    def append(self, value):
        newNode = Node(value)
        tailNode = self.tail
        if tailNode:
            return tailNode
        else:
            self.head = newNode
            self.tail = newNode
            return 
        

        newNode.prev = tailNode
        tailNode.next = newNode
        self.tail = newNode

    def remove(self, node: Node):
        previous = node.prev
        next = node.next
        if previous:
            previous.next = next 
        else:
            self.head = next

        next.prev = previous
        if next == None:
            self.tail = previous
        
        node.prev = None
        node.next = None
        return node.value


