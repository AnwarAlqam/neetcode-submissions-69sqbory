class Deque:

    class LinkedList:

        class Node:
            def __init__(self, val):
                self.val: int = val
                self.next = None

        def __init__(self, val):
            self.head: Node = None
            self.tail: Node = None

        def remove(self, index: int) -> bool:
            # Empty list
            if self.head is None:
                return False

            # Remove head
            if index == 0:
                self.head = self.head.next
                if self.head is None:
                    # List became empty
                    self.tail = None
                return True

            i: int = 1
            cur = self.head.next
            prev = self.head
            while cur is not None and i < index:
                i += 1
                prev = cur
                cur = cur.next

            if cur is None:
                return False

            prev.next = cur.next

            if cur.next is None:
                self.tail = prev

            return True

        def insertHead(self, val) -> None:
            if self.head == None:
                self.head: Node = self.Node(val)
                self.tail = self.head
            else:
                new_head: Node = self.Node(val)
                new_head.next = self.head
                self.head = new_head

        def insertTail(self, val) -> None:
            if self.tail == None:
                new_tail: Node = self.Node(val)
                self.head = new_tail
                self.tail = new_tail
            else:
                new_tail: Node = self.Node(val)
                self.tail.next = new_tail
                self.tail = new_tail

        def get(self, index: int) -> int:
            cur = self.head
            i = 0
            while cur is not None and i < index:
                cur = cur.next
                i += 1
            if cur is None:
                return -1
            return cur.val

    
    def __init__(self):
        self.size = 0
        self.linked_list: LinkedList = self.LinkedList(self)

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        self.linked_list.insertTail(value)
        self.size += 1

    def appendleft(self, value: int) -> None:
        self.linked_list.insertHead(value)
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        val: int = self.linked_list.get(self.size - 1)
        self.linked_list.remove(self.size - 1)
        self.size -= 1
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        val: int = self.linked_list.get(0)
        self.linked_list.remove(0)
        self.size -= 1
        return val
        
