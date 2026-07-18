class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        # Use the Bellman-Ford algorithm (go one step at a time and update the costs until k+1)
        for i in range(k+1):
            tmpPrices = prices.copy()

            for s, d, price in flights:
                if prices[s] == float("inf"):
                    continue
                
                # update the tmpPrices here with calculations
                if prices[s] + price < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + price
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]
