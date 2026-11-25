class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsMap = set()

        for n in nums:
            if n in numsMap:
                return True
            numsMap.add(n)
        
        return False