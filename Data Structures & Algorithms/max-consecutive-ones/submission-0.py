class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        consecutive_ones = 0

        for i in nums:
            if i != 1:
                max_consecutive_ones = max(consecutive_ones, max_consecutive_ones)
                consecutive_ones = 0
            elif i == 1:
                consecutive_ones += 1
                max_consecutive_ones = max(consecutive_ones, max_consecutive_ones)

        return max_consecutive_ones