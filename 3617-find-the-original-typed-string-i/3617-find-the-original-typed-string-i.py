class Solution:
    def possibleStringCount(self, word: str) -> int:
        resMap = defaultdict(int)
        resSet = set(word[0])
        i = 0

        for c in word:
            if c in resSet:
                resMap[(c,i)] += 1
            else:
                print(resSet)
                resSet.clear()
                i += 1
                resSet.add(c) 
                resMap[(c,i)] += 1   

        res = 1

        for v in resMap.values():
            res += (v-1)

        return res                    
        