class MyHashSet:

    def __init__(self):
        self.occurrences = defaultdict(int)

    def add(self, key: int) -> None:
        if not self.occurrences[key]:
            self.occurrences[key] += 1

    def remove(self, key: int) -> None:
        if self.occurrences[key]:
            del self.occurrences[key]

    def contains(self, key: int) -> bool:
        if self.occurrences[key]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)