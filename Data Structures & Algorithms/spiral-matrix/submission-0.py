class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) # We keep the right pointer outside by 1
        top, bottom = 0, len(matrix) # We keep the bottom pointer outside by 1

        while left < right and top < bottom:

            # Get all the top elements
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # Get all the right elements
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            # Check, in the cases with row/column vectors
            if not (left < right and top < bottom):
                break
            
            # Get all bottom elements
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            # Get all left elements
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
            
