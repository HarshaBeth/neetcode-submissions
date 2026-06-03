class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = {}

        # for i in range(len(nums)):
        #     counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        # # This is O(N log N), we can do better O(N log k) which can be done by using heapq
        # sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        # res = []
        # for i in range(k):
        #     res.append(sorted_counts[i][0])
        
        # return res

        # Bucket sort
        count = {}

        # Get count for each number
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        # Sorting
        freq = [[] for i in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res) == k):
                    return res




