class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0 for j in range(len(text2)+1)] for i in range(len(text1)+1) ]

        # i = rows, j = cols
        #   text 2
        # [0 0 0 0] 0  text 1
        # [0 0 0 0] 0  text 1
        # [0 0 0 0] 0  text 1
        #  0 0 0 0  0


        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # diagonal
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # Get the max of down and right
        
        return dp[0][0]