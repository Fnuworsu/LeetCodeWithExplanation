class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def perimeter(r,c):
            nonlocal p

            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if (nr not in range(rows)) or (nc not in range(cols)):
                    continue
                if grid[nr][nc] == 1:
                    p += 1
           
        res, p = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 4
                    perimeter(r,c)
    
        return res - p               

        