class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        map1 = {}

        for w in s1:
            if w not in map1:
                map1[w] = [1,0]
            else:
                map1[w][0] += 1

        for w in s2:
            if w not in map1:
                map1[w] = [0,1]
            else:
                map1[w][1] += 1   

        res = []

        for k,v in map1.items():
            if v[0] + v[1] == 1:
                res.append(k)

        return res                     
                    
        