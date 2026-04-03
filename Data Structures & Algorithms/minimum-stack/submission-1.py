class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        minimum = self.stack[0]
        for i in self.stack:
            if i < minimum:
                minimum = i

        return minimum