class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        """
        = {
            a
        }
        abc, bca
        key = [0,0,0,0]
        aaabc = [3,1,1]
        abaca = [3,1,1]

        ([3,1,1]) : [].add(w)
        """
        asci = lambda x: ord(x)-ord('a')

        for w in strs:
            key = [0] * 26
            
            for c in w:
                key[asci(c)] += 1

            resMap[tuple(key)].append(w)  

        return list(resMap.values())   
        