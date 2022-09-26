import linkedList

myList = linkedList.LinkedList()


def getMid(self, list:myList):
    slow = self.head
    fast = self.head

    if self.head is not None:
            while (fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
                print("The middle element is: ", slow.value)
myList.push(4)
myList.push(3)
myList.push(2)
myList.push(1)

getMid(myList)