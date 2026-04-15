class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, len(nums) - 1

        while i != len(nums) - 1:

            if nums[i] == nums[j] and abs(i - j) <= k: return True
            if j - 1 == i:
                i += 1
                j = len(nums) - 1
                continue

            j -= 1
            

        return False