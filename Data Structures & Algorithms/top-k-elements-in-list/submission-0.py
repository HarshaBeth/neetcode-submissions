class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_counts[i][0])
        
        return res