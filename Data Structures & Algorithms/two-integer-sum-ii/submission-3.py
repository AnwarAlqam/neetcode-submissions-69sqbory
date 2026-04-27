class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0,len(numbers) - 1
        if len(numbers) == 2:
            return [1, 2]

        while i < j:
            # if target < numbers[j]:
            #     j -= 1
            #     continue
            
            # if target > numbers[i]:
            #     i += 1
            #     continue

            print(f"numbers[i]: {numbers[i]} | numbers[j]: {numbers[j]}")
            if numbers[i] + numbers[j] == target and i < j:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                print("here")
                j -= 1

        return [-1, -1]