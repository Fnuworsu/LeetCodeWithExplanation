class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """
        R = [2,1,1,1]
        C = [1,1,2,1]

        """
        rows, cols = len(grid), len(grid[0])

        R = [0] * rows
        C = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    R[r] += 1
                    C[c] += 1
        
        servers = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if R[r] > 1 or C[c] > 1:
                        servers += 1

        return servers
        