class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        def canFlow(r, c, acc):
            if (r, c) in acc:
                return
            
            acc.add((r, c))

            dirs = [[1,0], [0,1], [-1,0], [0, -1]]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (not nr in range(rows) or
                    not nc in range(cols) or
                    heights[nr][nc] < heights[r][c]):
                    continue

                canFlow(nr, nc, acc)

        rows, cols = len(heights), len(heights[0])        

        pacific = set()
        for r in range(rows):
            canFlow(r, 0, pacific)
        for c in range(cols):
            canFlow(0, c, pacific)

        atlantic = set()
        for r in range(rows):
            canFlow(r, cols-1, atlantic)
        for c in range(cols):
            canFlow(rows-1, c, atlantic)

        # print((pacific.intersection(atlantic)))

        return list(pacific.intersection(atlantic))                            
        