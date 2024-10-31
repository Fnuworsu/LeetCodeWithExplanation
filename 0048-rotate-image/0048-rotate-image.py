class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #reverse the matrix
        """
        1 2 3
        -----
        7 8 9
        gives

        7 8 9
        4 5 6
        1 2 3

        transpose

        * 8 9
        4 * 6
        1 2 *

        gives
        7 4 1
        8 5 2
        9 6 3
        """
        l, r = 0, len(matrix) - 1
        #reverse the matrix row by row
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]

            l += 1
            r -= 1
        # print("After rotation")    
        # print(matrix)
        # print()
        #method to find the transpose of a matrix
        for i in range(len(matrix)):
            # print(i)
            # print()
            for j in range(i):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
                # print(matrix)  
                # print() 