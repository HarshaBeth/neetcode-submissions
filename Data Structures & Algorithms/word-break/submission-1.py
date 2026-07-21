class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP go backwards. Start with a base case of True which is outside the index range.
        # If the word from the dictionary is exactly from the word till the next 'True', then we set it
        # also to True, otherwise if the word is not completely reaching the next True, it takes the 
        # false value of the dp[i + len(w)] index
        # e.g. car | s, since s is False then c index also becomes False and this goes till the 0th index.

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]: # break if its true
                    break
        
        return dp[0]