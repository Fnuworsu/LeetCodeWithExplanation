class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        
        def sim(w, ret):
            l = 0
            summ = 0

            for r in range(len(w)):
                summ += int(w[r])

                if (r-l+1) == k:
                    ret += str(summ)
                    summ = 0
                    l = r + 1
            
            if l <= r:
                ret += str(summ)
            
            return ret

        
        res = ""

        while len(s) > k:
            res = sim(s, "")

            if len(res) > k:
                s = res
                res = ""
            else:
                return res