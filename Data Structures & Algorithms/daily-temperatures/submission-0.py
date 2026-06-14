class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tempVal, tempIdx = stack.pop()
                res[tempIdx] = (i - tempIdx)
            stack.append([temp, i])
        
        return res