class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for x in range(n)] for y in range(n)]
        row = n

        cSet = set()
        dSet = set()
        aSet = set()

        res = []

        def placeQueen(r, cSet, dSet, aSet):
            nonlocal res
            if r == row:
                res.append(["".join(x) for x in board])
                return

            for c in range(row):
                if c in cSet or r+c in dSet or r-c in aSet:
                    continue
                cSet.add(c)
                dSet.add(r+c)
                aSet.add(r-c)

                board[r][c] = "Q"
                #include
                placeQueen(r+1, cSet, dSet, aSet)

                cSet.remove(c)
                dSet.remove(r+c)
                aSet.remove(r-c)
                #exclude
                board[r][c] = "."

        placeQueen(0, cSet, dSet, aSet)

        return res
        