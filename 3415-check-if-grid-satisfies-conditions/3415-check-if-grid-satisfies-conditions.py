class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        outBounds = lambda r,c: r < 0 or r > rows-1 or c < 0 or c > cols-1
        dirs = [(1,0), (0,1)]

        def check(r,c):
            for dr,dc in dirs[:1]:
                nr, nc = r + dr, c + dc

                if outBounds(nr,nc):
                    continue 
                if grid[r][c] != grid[nr][nc]:
                    return False
            
            for dr,dc in dirs[1:]:
                nr, nc = r + dr, c + dc

                if outBounds(nr,nc):
                    continue 
                if grid[r][c] == grid[nr][nc]:
                    return False

            return True
        
        for r in range(rows):
            for c in range(cols):
                if not check(r,c):
                    return False
        
        return True