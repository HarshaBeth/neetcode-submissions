class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # nums = [1] + [num for num in nums if num != 0] + [1]
        # dp = {}

        # def dfs(l, r):
        #     if l > r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]
            
        #     dp[(l, r)] = 0
        #     for i in range(l, r+1):
        #         coins = nums[l-1] * nums[i] * nums[r+1] 
        #         coins += dfs(l, i-1) + dfs(i+1, r)
        #         dp[(l, r)] = max(dp[(l, r)], coins)
            
        #     return dp[(l, r)]
        
        # return dfs(1, len(nums)-2)

        nums = [1] + [num for num in nums if num != 0] + [1]
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        def dfs(l, r):
            if l > r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            result = 0

            for i in range(l, r + 1):
                coins_from_i = nums[l - 1] * nums[i] * nums[r + 1]

                left_coins = dfs(l, i - 1)
                right_coins = dfs(i + 1, r)

                result = max(
                    result,
                    left_coins + coins_from_i + right_coins
                )

            dp[l][r] = result
            return result

        return dfs(1, n - 2)