class MyStack:

    class Node:

        def __init__(self, val: int):
            self.val: int = val
            self.next: Node = None

    class Queue:

        def __init__(self):
            self.head: MyStack.Node = None
            self.tail: MyStack.Node = None
            self.size: int = 0

        def append(self, val: int) -> None:
            new_node: MyStack.Node = MyStack.Node(val)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.size += 1

            self.printQueue()

        def pop(self) -> int:
            val: int = self.head.val
            self.head = self.head.next
            self.size -= 1

            self.printQueue()
            return val

        def getTail(self) -> MyStack.Node:
            return self.tail

        def printQueue(self) -> None:
            cur = self.head
            arr = []
            while cur != None:
                arr.append(str(cur.val))
                cur = cur.next

            print(", ".join(arr))

    def __init__(self):
        self.queue: Queue = self.Queue()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        size: int = self.queue.size
        for i in range(size - 1):
            val: int = self.queue.pop()
            self.queue.append(val)

        return self.queue.pop()

    def top(self) -> int:
        return self.queue.getTail().val

    def empty(self) -> bool:
        return self.queue.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()