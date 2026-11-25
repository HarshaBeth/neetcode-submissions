class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = {}

        # Get the counts
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        # Sort counts
        sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_counts[i][0])
        
        return res
