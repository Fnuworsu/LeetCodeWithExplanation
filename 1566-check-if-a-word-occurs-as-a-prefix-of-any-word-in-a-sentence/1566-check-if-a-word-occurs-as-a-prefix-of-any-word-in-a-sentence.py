class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = []
        i = 1

        for word in sentence.split():
            prefix = ""

            for c in word:
                prefix += c
                if prefix == searchWord:
                    res.append(i)
                    break
            
            i += 1
        
        res.sort()

        return res[0] if res else - 1
        