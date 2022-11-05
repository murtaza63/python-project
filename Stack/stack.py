class Stack:
    # Creating Stack
    def stackData(self):
        """
        Stack main function
        """
        stack = []
        return stack

    def push(self, stack, item):
        return stack.append(item)

    # Removing an element from the stack
    def remove(self, stack):
        if self.checkEmpty(stack) == True:
            return "stack is empty"
        return stack.pop()

    # Creating an empty stack
    def checkEmpty(self, stack):
        if len(stack) == 0:
            return True
        return False

    # Checking the size of the stack
    def checkSize(self, stack):
        return len(stack)

    def checkPeek(self, stack):
        if self.checkEmpty(stack):
            return "Stack is empty so there is no peek element"
        return stack[-1]


# driver code
MyStack = Stack()
createStack = MyStack.stackData()

MyStack.push(createStack, 1)
MyStack.push(createStack, 2)
MyStack.push(createStack, 3)
MyStack.push(createStack, 4)

# Stack before remove
print(MyStack)
MyStack.remove(createStack)

print("Size of stack", MyStack.checkSize(createStack))


print("Removed element from stack is", MyStack.remove(createStack))

print("\n========Return True if the stack is empty otherwise return False=====:")
print(MyStack.checkEmpty(createStack))
print(" \nThe top element of the stack is", MyStack.checkPeek(createStack))
print(createStack)
