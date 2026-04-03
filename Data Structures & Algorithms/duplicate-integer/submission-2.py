class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if len(nums) <= 1:
            return False

        for i in range(1, len(nums), 1):
            if nums[i - 1] == nums[i]:
                return True

        return False