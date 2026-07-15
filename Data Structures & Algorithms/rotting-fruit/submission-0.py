class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time = fresh = 0

        # First, find the no. of fresh oranges and the coordinates of the rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        # Second, do BFS and add time as you proceed
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    # If not fresh or out of bounds then skip this cell
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                        continue

                    # Now that we know it's fresh, rot it
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1



