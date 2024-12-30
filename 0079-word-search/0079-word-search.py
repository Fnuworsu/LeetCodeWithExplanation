class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def valid(r,c):
            return 0 <= r < rows and 0 <= c < cols
        """
        set if seen
        """
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def backtrack(i,r, c, seen):
            #find the words till the end and return true if found else return false
            if i == len(word):
                return True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if valid(nr,nc) and (nr,nc) not in seen:
                    if board[nr][nc] == word[i]:
                        seen.add((nr,nc))
                        if backtrack(i+1,nr,nc, seen):
                            return True
                        seen.remove((nr,nc))   
            return False                 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(1,r,c, {(r,c)}):
                    return True

        return False                


        