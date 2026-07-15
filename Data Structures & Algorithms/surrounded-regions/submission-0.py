class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def convertT(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            convertT(r+1, c)
            convertT(r-1, c)
            convertT(r, c+1)
            convertT(r, c-1)

        # 1. Convert the border O's to a T
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    convertT(r, c)

        # 2. Capture all O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O": board[r][c] = "X"

        # 3. Convert the T's to O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T": board[r][c] = "O"