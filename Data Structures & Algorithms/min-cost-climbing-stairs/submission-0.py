class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            v1 = cost[i] + cost[i+1]
            v2 = cost[i] + cost[i+2]

            cost[i] = min(v1, v2)
        
        return min(cost[0], cost[1])

