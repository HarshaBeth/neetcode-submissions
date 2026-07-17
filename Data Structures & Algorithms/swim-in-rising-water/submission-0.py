class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]] # height, row, col

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minHeap:
            height, r, c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return height

            for dr, dc in directions:
                neiRow, neiCol = r + dr, c + dc
                if neiRow < 0 or neiCol < 0 or neiRow == N or neiCol == N or (neiRow, neiCol) in visit:
                    continue
                visit.add((neiRow, neiCol))
                heapq.heappush(minHeap,[max(grid[neiRow][neiCol], height) , neiRow, neiCol])
