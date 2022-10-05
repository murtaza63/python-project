

from collections import deque


def reversedQueue(queue):

    Stack  =  []

    while (queue):
        Stack.append(queue[0])
        queue.popleft()
    while (len(Stack) != 0):
        queue.append(Stack[-1])
        Stack.pop()


if __name__ == "__main__":
    queue = deque([10,20,30,40,50,60,70,80,90,100])
    reversedQueue(queue)
    print(queue)
