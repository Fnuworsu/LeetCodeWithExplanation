class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # visited = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()
                dirs = [(1,0), (0,1), (-1,0), (0,-1)]

                for dr,dc in dirs:
                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nr > rows-1 or nc < 0 or nc > cols-1 or grid[nr][nc] == '0':
                        continue

                    q.append((nr,nc))
                    grid[nr][nc] = '0'

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r,c)

        return res                            


