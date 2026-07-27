class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # First we determine which rows/cols need to be zeros
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Set the column index to 0
                
                    if r > 0:
                        matrix[r][0] = 0 # Set the row index to 0 if r is not first row
                    else:
                        rowZero = True
        
        # Leave the first row/col because they are our indicators
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Let's change the first column now (that's why we had first row index separate)
        if matrix[0][0] == 0: # First column is zero
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Now we change the first row IF we had it set to zero via boolean
        if rowZero:
            for c in range(COLS):  
                matrix[0][c] = 0
                