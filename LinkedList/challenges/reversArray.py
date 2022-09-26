# 1st challenge print in reverse 
print("Print in reverse challenge")
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printInReverse(self, temp):
        if temp:
            self.printInReverse(temp.next)
            print(temp.value, end=' ')
        else:
            return 
    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
    # get midle element
    def getMid(self):
        slow = self.head
        fast = self.head

        if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
                print("The middle element is: ", slow.value)

        


list3 = LinkedList()
list3.push(5)
list3.push(4)
list3.push(3)
list3.push(2)
list3.push(1)



list3.getMid()

    



