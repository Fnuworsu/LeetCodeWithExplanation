class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        interval = firstList + secondList
        interval.sort(key=lambda x:x[0])

        row = interval[0] #[s,e]
        res = []

        for s, e in interval[1:]:
            #overlap
            if row[1] == s:
                s1 = s
                e1 = row[1]
                res.append([s1, e1])
                if row[1] < e:
                    row = [s, e]

            elif row[1] > s:
                s1 = max(row[0], s)
                e1 = min(row[1], e)
                res.append([s1,e1])
                if row[1] < e:
                    row = [s, e]

            else:
                row = [s,e]

        return res                



        