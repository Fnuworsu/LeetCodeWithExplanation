class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            pivot_idx = (l + r) // 2
            pivot_elem = matrix[pivot_idx // cols][pivot_idx % cols]

            if target == pivot_elem:
                return True
            else:
                if target < pivot_elem:
                    r = pivot_idx - 1
                else:
                    l = pivot_idx + 1
        
        return False