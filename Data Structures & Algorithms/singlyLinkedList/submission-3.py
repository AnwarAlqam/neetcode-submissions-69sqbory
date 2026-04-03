class LinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head == None:
            return -1

        if index == 0:
            return self.head.value

        i: int = 1
        cur = self.head.next
        while cur.next != None:
            if i == index:
                break
            cur = cur.next
            i += 1

        if i != index:
            return -1

        print(f"i: '{i}'")
        self.printList()
        print(f"Got '{cur.value}' at index '{index}'")
        print("\n")
        return cur.value

    def printList(self) -> None:
        print(", ".join(self.getValuesStr()))

    def insertHead(self, val: int) -> None:
        if not self.head:
            new_head: Node = self.Node(val)
            self.head = new_head
            self.tail = self.head
        else:
            new_head: Node = self.Node(val)
            new_head.next = self.head
            self.head = new_head

    def insertTail(self, val: int) -> None:
        if self.tail == None:
            new_tail: Node = self.Node(val)
            self.head = new_tail
            self.tail = self.head
        else:
            new_tail: Node = self.Node(val)
            self.tail.next = new_tail
            self.tail = new_tail

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

    def getValues(self) -> List[int]:
        values = []

        cur = self.head
        while cur != None:
            values.append(cur.value)
            cur = cur.next

        return values

    def getValuesStr(self) -> List[int]:
        values = []

        cur = self.head
        while cur != None:
            values.append(str(cur.value))
            cur = cur.next

        return values

