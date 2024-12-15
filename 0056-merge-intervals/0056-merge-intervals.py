class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,8] [2,6] [8,10] [15,18]
        overlap = [1,8] [2,6] s=min e= max [1,6]
        []
        """
        intervals.sort()
        row = intervals[0]
        res = []

        for s,e in intervals[1:]:
            #overlap
            if row[1] >= s:
                row[1] = max(row[1], e)
            else:
                res.append(row)
                row = [s,e]
        #excess        
        res.append(row)
        return res            

        