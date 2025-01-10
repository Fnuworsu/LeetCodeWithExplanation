class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        {
            e : {e:1},
            o : {o:1}
        }

        {
            amazon : {a:2, m:1, z:1, o:1, n:}
        }
        if 
        """
        hmap = defaultdict(int)
        res = []

        for w2 in words2:
            freq = Counter(w2)
            for k in freq.keys():
                hmap[k] = max(freq[k], hmap[k])

        print(hmap)        

        for w1 in words1:
            freq = Counter(w1)
            b = 1
            for k in hmap:
                if freq[k] < hmap[k]:
                    b = 0
                    break
            
            if b: res.append(w1)  

        return res               
        