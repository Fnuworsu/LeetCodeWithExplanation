class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        resMap = {}

        for w in words1:
            if w not in resMap:
                resMap[w] = [1,0]
            else:
                resMap[w][0] += 1

        for w in words2:
            if w not in resMap:
                resMap[w] = [0,1]
            else:
                resMap[w][1] += 1 

        res = 0

        for v in resMap.values():
            if v[0] == v[1] == 1:
                res += 1

        return res                       

        