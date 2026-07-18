class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 will skip the previous house, rob2 is the current house
        # old best, new best
        rob1, rob2 = 0, 0 

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

