class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # ============ RECURSION ==================
        # cache = {}

        # # j is the t(second word) and i is the s(first word)
        # def dfs(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     if s[i] == t[j]:
        #         cache[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
        #     else:
        #         cache[(i,j)] = dfs(i+1, j)
        #     return cache[(i, j)]
        
        # return dfs(0, 0)

        # ============ DP ==================
        dp = [[0] * (len(t) + 1) for i in range(len(s)+1)]
        
        # right side is all 1s since any s can produce  an empty t ("")
        for i in range(len(s)+1):
            dp[i][len(t)] = 1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                dp[i][j] = dp[i+1][j] # If we skip s[i] cuz of no match

                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j] # Ways after selecting current and skipping current s[i]

        return dp[0][0]






