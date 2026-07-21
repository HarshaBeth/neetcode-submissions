class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep track of current MAX and current MIN while traversing through the list
        # Because the extreme highs/lows can possibly give the best next product when multiplied
        # if we reach 0, set current Max and current Min to 1

        res = max(nums)
        currentMax = currentMin = 1

        for n in nums:
            if n == 0:
                currentMax, currentMin = 1, 1
            
            temp = n * currentMax
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(temp, n * currentMin, n)

            res = max(res, currentMax)
        return res