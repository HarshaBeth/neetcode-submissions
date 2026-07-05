class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Do left of branch that includes the i'th number
            subset.append(nums[i])
            dfs(i + 1)

            # Do right of branch that does NOT include
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res