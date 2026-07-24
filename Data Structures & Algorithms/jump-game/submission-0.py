class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Can be solved using DP Top down memoization
        # But below is Greedy solution

        goal = len(nums)-1 # Goal is the index, not its value

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False