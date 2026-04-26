class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        if len(nums) > 1 and nums[len(nums)  - 1] == nums[len(nums) - 2]:
            nums.pop(len(nums) - 1)

        return len(nums)