class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def outBounds(r,c):
            return r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == '0'

        def bfs(r,c):
            q = deque([(r,c)]) 

            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    grid[r][c] = '0'

                    for dr,dc in dirs:
                        nr, nc = r + dr, c + dc

                        if outBounds(nr,nc):
                            continue
                        
                        q.append((nr,nc))
                        grid[nr][nc] = '0'
        
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r,c)
        
        return count


            