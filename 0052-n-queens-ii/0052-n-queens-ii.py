class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        optimised space complexity
        """
        board = [["." for x in range(n)] for y in range(n)]
        row = n

        cSet = set()
        dSet = set()
        aSet = set()
        
        res = 0

        def placeQueen(r, cSet, dSet, aSet):
            nonlocal res
            #base case
            if r == row:
                res += 1
                return

            for c in range(row):
                if c in cSet or r+c in dSet or r-c in aSet:
                    continue
                cSet.add(c)
                dSet.add(r+c)
                aSet.add(r-c)

                board[r][c] = "Q"
                placeQueen(r+1, cSet, dSet, aSet)
                board[r][c] = "."

                cSet.remove(c)
                dSet.remove(r+c)
                aSet.remove(r-c)

        placeQueen(0, cSet, dSet, aSet)                
        
        return res 
        