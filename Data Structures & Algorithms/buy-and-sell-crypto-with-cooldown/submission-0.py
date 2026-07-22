class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # States: buying, selling. Cooldown is not a state, it is a path (to the right of tree)
        # We are doing DFS, with caching
        # if Buy: i+1 (cuz you MIGHT sell next)
        # if Sell: i+2 (cuz of cooldown)

        dp = {} # key: (i, buying(boolean)), value: maxProfit


        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # This is one path, so 'buying' stays the same we just skip current node
            cooldown = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i] # basically when we buy we subtract our money
                dp[(i, buying)] = max(cooldown, buy)
            else:
                sell = dfs(i+2, not buying) + prices[i] # here add the money to our total
                dp[(i, buying)] = max(cooldown, sell)
            return dp[(i, buying)]
        
        return dfs(0, True)
