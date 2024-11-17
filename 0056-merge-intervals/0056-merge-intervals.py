class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        row = intervals[0]

        for s, e in intervals[1:]:
            if row[1] >= s:
                row[1] = max(row[1], e)
            else:
                res.append(row)
                row = [s, e]
        #rem
        res.append(row) 

        return res            

        