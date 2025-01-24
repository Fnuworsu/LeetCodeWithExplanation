class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def isBound(r,c):
            return 0 <= r < rows and 0 <= c < cols and board[r][c] == "O"

        def dfs(r,c):
            board[r][c] = "#"
            
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr,dc in dirs:
                nr, nc = r + dr, c + dc
                if isBound(nr,nc):
                    dfs(nr,nc)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
            