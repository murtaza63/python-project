from collections import deque


def DoubleEndedQueue():
    stack = []
    queue = deque([1,2,3,4,5,6,7])
    while queue:
        element = queue.pop()
        
        stack.append(element)
    print(stack)


DoubleEndedQueue()
