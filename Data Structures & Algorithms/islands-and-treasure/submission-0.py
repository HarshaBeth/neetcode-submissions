class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def addRoom(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == -1 or (r, c) in visit):
                return
            
            q.append([r, c])
            visit.add((r, c))

        # First find the gates
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # Second, simultaneously add distances from the gates in BFS manner
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1
        
