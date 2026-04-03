class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack
        print(self.stack)

    def pop(self) -> None:
        print(f"before pop: '{self.stack}'")
        self.stack.pop(0)
        print(f"after pop: '{self.stack}'")

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        print(self.stack[0])
        minimum = self.stack[0]
        for i in self.stack:
            if i < minimum:
                minimum = i

        return minimum