class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        longest = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in setNums:
                length = 0
                while (nums[i]+length) in setNums:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
            