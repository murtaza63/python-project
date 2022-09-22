from linkedList import LinkedList


def example(description):
    print("---Example of ", description, "---")
    LL = LinkedList()
    LL.push(3)
    LL.push(2)
    LL.push(1)
    print(LL.printLL())
