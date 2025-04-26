class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        i = 0

        for r in range(m):
            for c in range(n):
                matrix[r][c] = original[i]
                i += 1
        
        return matrix
