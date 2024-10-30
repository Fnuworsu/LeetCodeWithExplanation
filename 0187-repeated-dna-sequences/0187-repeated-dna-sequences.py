class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        start, end = A, C
        so when i meer another A, start of a new sequesnce: append previous

        what is sequence?
         sequence = 10
        
        
        res = []
        acc = "" (AAAAACCCCC)
        AAAAACCCCC AAAAACCCCCC AAAAA GGGTTT
         l
                   r 
        AAAAA CCCCCAAAAA CCCCCCAAAAA GGGTTT
       """
        if len(s) < 10:
            return []
        # if len(s) == 10:
        #     return s.plit(s)    

        hashMap = defaultdict(int)
        acc = deque([])

        for r in range(len(s)):
            if len(acc) ==10:
                # print(acc)
                hashMap[tuple(acc)] += 1
                acc.popleft()
                # acc.append(s[r])
            
            acc.append(s[r])    
            # print(acc)
        if len(acc) == 10: #add any leftover sequence <= 10
            hashMap[tuple(acc)] += 1  
              
        res = []
        for k, v in hashMap.items():
            if v > 1:
                res.append("".join(list(k)))

        # print(res)
        return res                    



        