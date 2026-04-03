class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        for i in range(0, len(arr) - 1, 1):
            max_value = 0
            for j in range(i + 1, len(arr), 1):
                max_value = max(arr[j], max_value)

            arr[i] = max_value

        arr[len(arr) - 1] = -1
        return arr