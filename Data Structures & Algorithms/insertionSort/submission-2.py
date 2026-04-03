# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res: List[List[Pair]] = []
        n = len(pairs)

        if n == 0:
            return []

        # Append the initial state
        res.append(pairs[:])

        for i in range(1, n):
            j = i - 1
            # Move elements greater than the key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            # Snapshot the state after inserting element i
            res.append(pairs[:])

        return res