from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Stack(Generic[T]):
# Creating Stack
    def __init__(self, elements: list[T]):
        self.elements = elements or []
    # Adding items into the stack
    def push(self,element: T):
        self.elements.append(element)
    #Removing an element from the stack
    def pop(self) -> Optional[T]:
        return self.elements.pop() if self.elements else None

    def peek(self) -> Optional[T]:
        return self.elements[-1] if self.elements else None

    def is_empty(self) -> bool:
        return self.peek() is None
    def __bool__(self) -> bool:
        return bool(self.elements)

    def __str__(self):
        stack_as_str = "\n".join(lambda x: str(x), reversed(self.elements))
        return f"""
        ----top----
        {stack_as_str}
        -----------
        """



    #Examples 

MyStack = Stack()
createStack = MyStack.stackData()

MyStack.push(createStack, 1)
MyStack.push(createStack, 2)
MyStack.push(createStack, 3)
MyStack.push(createStack, 4)

MyStack.remove(createStack)

print("Size of stack", MyStack.checkSize(createStack))


print("Removed element from stack is", MyStack.remove(createStack))

print("\n========Return True if the stack is empty otherwise return False=====:")
print(MyStack.checkEmpty(createStack))
print(" \nThe top element of the stack is", MyStack.checkPeek(createStack))
print(createStack)
    