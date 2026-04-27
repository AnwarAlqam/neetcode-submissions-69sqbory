class Solution:
    def checkIndices(self, i, j, k):
        if i == j and i == k and j == k:
            return True
        return False
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0 and nums[0]:
                res.append([nums[0], nums[1], nums[2]])
            return res

        for i in range(0, len(nums), 1):
            j,k = i + 1, len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0 and not self.checkIndices(i, j, k):
                    arr = [nums[i], nums[j], nums[k]]
                    if arr not in res:
                        res.append(arr)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    j += 1
                    k -= 1
        return res