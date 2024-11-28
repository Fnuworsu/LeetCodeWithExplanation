class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        4 4 - 2 4 -2 -2 4 4 -2 4 -2 4 -2
        """
        row, col = len(grid), len(grid[0])
        res = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r-1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2

        return res                    
        