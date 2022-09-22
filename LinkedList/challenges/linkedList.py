



class Node:
    #constructor 
    def __init__(self, value, next=None):
        self.value = value
        self.next =  next 


    # A Linked List class with a single head node 
class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        
    
       
        

    # insert at the front of the linkedlist 
    def push(self,NewValue):
        new_node =  Node(NewValue)
        new_node.next = self.head
        self.head = new_node
        
    
    def append(self, new_value):
        
        new_node = Node(new_value)
        # if linkedlist is empty then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        # else traverse till the last node 
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node


    def node(self,index: int) -> Node:
        currentNode = self.head
        currentIndex = 0
        while currentNode is not None and currentIndex < index:
            currentNode  = currentNode.next
            currentIndex += 1
        return currentNode
    
    def insert(self,value, afterNode: Node):
        if self.next == afterNode:
            self.append(value)
            return self.next
    

    def pop(self):
        self.head = self.head.next
        if None:
            self.next = None
        return self.head.value
    

    def removeLast(self):
        if(self.head != None):
            if(self.head.next == None):
                return self.pop()
            else:
                prev = self.head
                current = self.head
                while(prev.next.next != None):
                    prev = prev.next
                lastNode =  prev.next
                prev.next = None
                lastNode = None


    def removeAfter( self, index):
        prev = self.head
        current = self.head.next
        for i in range(1, index - 1):
            current = current.next
            prev = prev.next
        prev.next = current.next


        

      
        

        
        
    

        
        


# print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next

MyList = LinkedList()
# MyList.push(3)
# MyList.push(2)
# MyList.push(1)
# MyList.append(4)

# print("Befor inserting", MyList.printLL())
# midleNode = MyList.node(2)
# for _ in range(1,4):
#     midleNode = MyList.insert(-1, midleNode)
# print("After inserting:", MyList.printLL())


# print(MyList.pop())
# MyList.removeLast()
# print("Removing middle node on list2")

# MyList.removeAfter(2)

# print(MyList.printLL())


def example(description):
    print("--- Example of ", description, "---")
   
    
    

# example("creating and linking nodes")
# node1 = Node(value= 1)
# node2 = Node(value= 2)
# node3 = Node(value= 3)
# node4 = Node(value= 4)
# node5 = Node(value= 5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# print(node1)
example("push")
list1 = LinkedList()
list1.push(4)
list1.push(3)
list1.push(2)
list1.push(1)
print(list1.printLL())

example("append")
list2 = LinkedList()
list2.append(1)
list2.append(2)
list2.append(3)
print(list2.printLL())
  




