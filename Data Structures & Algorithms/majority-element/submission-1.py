class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ocurrances = defaultdict(int)

        for num in nums:
            ocurrances[num] += 1

        max_combo = max(ocurrances.items(), key=lambda x: x[1])

        return max_combo[0]