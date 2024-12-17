class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 0: return False

        l, r = 0, rows * cols - 1

        while l <= r:
            pivotIdx = (l+r) // 2
            pivotEl = matrix[pivotIdx // cols][pivotIdx % cols]

            if target == pivotEl:
                return True
            else:
                if pivotEl > target:
                    r = pivotIdx - 1
                else:
                    l = pivotIdx + 1    

        return False                
        