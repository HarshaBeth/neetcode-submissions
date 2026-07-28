class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = n ^ res # ^ this is the XOR operation and compares bits (e.g. 010 ^ 100 = 110)
        
        return res