class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for x in range(n)] for y in range(n)]
        rSet, cSet, aSet, dSet = set(), set(), set(), set()
        row = n
        res = 0

        def backtrack(r, rSet, cSet, aSet, dSet):
            nonlocal res

            if r == row:
                res += 1
                return

            for c in range(row):
                if r in rSet or c in cSet or r+c in dSet or r-c in aSet:
                    continue

                rSet.add(r)
                cSet.add(c)
                dSet.add(r+c)
                aSet.add(r-c)

                board[r][c] = 'Q'
                backtrack(r+1, rSet, cSet, aSet, dSet)
                board[r][c] = '.'

                rSet.remove(r)
                cSet.remove(c)
                dSet.remove(r+c)
                aSet.remove(r-c)

        backtrack(0, rSet, cSet, aSet, dSet)

        return res               

        