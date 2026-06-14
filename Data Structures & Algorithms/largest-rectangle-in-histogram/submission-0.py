class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i-idx))
                start = idx
            
            stack.append((start, h))
        

        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)
        
        return maxArea
        