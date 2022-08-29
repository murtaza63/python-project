


def stackData():
    stack = []
    return stack
def push(stack, item):
    return stack.append(item)
def remove(stack):
    if checkEmpty(stack) == True:
        return "stack is empty"
    return stack.pop()
def checkEmpty(stack):
    if len(stack) == 0:
        return True
    return False
def checkSize(stack):
    return len(stack)

def checkPeek(stack):
    if checkEmpty(stack):
        return "Stack is empty so there is no peek element"
    return stack[-1]



creackStack = stackData()
push(creackStack, 1)
push(creackStack, 2)
push(creackStack, 3)
push(creackStack, 4)

remove(creackStack)

print("Size of stack", checkSize(creackStack))


print("Removed element from stack is", remove(creackStack))

print("========Return True if the stack is empty otherwise return False=====")
print(checkEmpty(creackStack))
print(" The top element of the stack is", checkPeek(creackStack))
