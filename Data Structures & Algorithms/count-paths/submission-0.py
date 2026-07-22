class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # This is the bottom row, all 1s
        # m = rows, n = cols
        
        # We go through the other rows, except the last row, hence m-1
        for i in range(m-1):
            newRow = [1] * n

            # we start from the 2nd last element to not deal with index out of range error and since we know the last column is always 1
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            
            row = newRow
        
        return row[0]