class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxMap = {} # number, index

        for i, n in enumerate(nums):
            if (target - n) in idxMap:
                return [idxMap.get(target-n), i]
            
            idxMap[n] = i