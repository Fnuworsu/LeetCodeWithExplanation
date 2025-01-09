class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #Brute Force
        s,e = 0, len(pref)
        res = 0

        for w in words:
            if len(w) < e:
                continue
            if w[0] != pref[0]:
                continue    
            if w[s:e] == pref:
                res += 1

        return res            
        