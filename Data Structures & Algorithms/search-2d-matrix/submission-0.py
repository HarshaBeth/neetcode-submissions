class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1

        while top <= bot:
            midRow = (top + bot) // 2

            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        
        if not top <= bot:
            return False
        row = (top+bot) // 2
        l, r = 0, COLS-1
        while l <= r:
            midIdx = (l+r) // 2

            if target > matrix[row][midIdx]:
                l = midIdx + 1
            elif target < matrix[row][midIdx]:
                r = midIdx - 1
            else:
                return True
        
        return False