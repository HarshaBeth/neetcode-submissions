class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            midIdx = (l + r) // 2

            if target > nums[midIdx]:
                l = midIdx+1
            elif target < nums[midIdx]:
                r = midIdx-1
            else:
                return midIdx
        
        return -1