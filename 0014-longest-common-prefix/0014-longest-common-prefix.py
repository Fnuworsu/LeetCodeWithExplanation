class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        [flower, flow, flight] => "fl"    
        =>
        [flower,flight,flow]
        flower, 
              
        """
        strs.sort()
        first = strs[0] #samllest length
        last = strs[-1] #greatest length

        print(strs)
        res = ""

        for i in range(0, len(first)):
            if first[i] != last[i]:
                return res
            res += first[i]

        return res        
