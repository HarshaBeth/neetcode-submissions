class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up approach - the TRUE DP solution
        # dp stores how many WAYS there are to solve for each amount
        dp = [amount+1] * (amount+1)
        dp[0] = 0 # it takes 0 coins to have a sum of 0

        # a means amount
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1