class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def outBounds(r,c):
            return r < 0 or r > rows-1 or c < 0 or c > cols-1 or grid[r][c] == 0
        
        def bfs(r,c):
            nonlocal res

            q = deque([(r,c)])
            seen = set()
            curr = 0

            while q:
                r,c = q.popleft()
                if (r,c) in seen:
                    continue
                seen.add((r,c))
                curr += grid[r][c]

                for dr,dc in dirs:
                    nr,nc = r + dr, c + dc
                    if outBounds(nr,nc) or (nr,nc) in seen:
                        continue
                    q.append((nr,nc))
            
            res = max(res, curr)
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    bfs(r,c)
        
        return res
