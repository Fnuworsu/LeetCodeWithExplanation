class Solution:
    def romanToInt(self, s: str) -> int:
        Map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900  
        }
        
        res = 0
        q = deque([])

        for c in s:
            if len(q) > 1:
                if q[0]+q[1] in Map:
                    res += Map[q.popleft() + q.popleft()]
                else:
                    res += Map[q.popleft()]
            q.append(c)

        while q:
            if len(q) > 1 and q[0]+q[1] in Map:
                res += Map[q.popleft()+q.popleft()]
            else:
                res += Map[q.popleft()]        
        return res            