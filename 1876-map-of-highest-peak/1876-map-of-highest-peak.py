class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        q = deque()
        dist = [[float("inf") for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    dist[r][c] = 0
        
        def isBound(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        while q:
            r,c = q.popleft()
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if isBound(nr,nc) and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr,nc))
    
        return dist
        