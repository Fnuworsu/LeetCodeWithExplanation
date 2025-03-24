class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        days = 10
        (1,3) (5,7) (9,10)

        1-3 = 3
        5-7 = 3
        9-10 = 2
        = 8
        1,3
        merge overlap
        then cout range inclusive
        1,3   2,4
        """
        meetings.sort()
        row = meetings[0]
        res = []

        for s,e in meetings[1:]:
            #overlap
            if row[1] >= s:
                row[1] = max(row[1], e)
            else:
                res.append(row)
                row = [s,e]
        
        if row:
            res.append(row)
        
        ans = 0

        for s,e in res:
            ans += (e-s+1)
        
        return days-ans


        