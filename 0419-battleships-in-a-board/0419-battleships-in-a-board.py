class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or board[r][c] == ".":
                return

            board[r][c] = "."

            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                dfs(nr,nc)

        res = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    res += 1
                    dfs(r,c)

        return res                      