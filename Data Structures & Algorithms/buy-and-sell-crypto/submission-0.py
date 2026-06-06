class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                res = prices[r] - prices[l]
                bestProfit = max(bestProfit, res)
            else:
                l = r
            
            r += 1            
        
        return bestProfit