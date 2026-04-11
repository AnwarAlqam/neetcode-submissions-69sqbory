class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        res = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        return [num for num, _ in res[:k]]