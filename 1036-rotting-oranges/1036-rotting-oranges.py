class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0

        pq = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    pq.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        def isBound(r,c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while pq and fresh > 0:

            for _ in range(len(pq)):
                r,c = pq.popleft()

                for dr,dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if isBound(nr,nc):
                        grid[nr][nc] = 2
                        fresh -= 1
                        pq.append((nr,nc))
                
            time += 1
        # print(time)
        return time if fresh == 0 else -1
                