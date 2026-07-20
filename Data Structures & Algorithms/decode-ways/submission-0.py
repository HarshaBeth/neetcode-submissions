class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s): 1}

        def dfs(i):
            # Base cases
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            # So we need to check the combination of i+1 and i+2 (if possible)
            res = dfs(i+1)

            if (i+1 < len(s) and (s[i] == "1"  or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            
            # Add it to the map since we will reuse in the recursion backwards
            dp[i] = res
            return res
        
        return dfs(0)