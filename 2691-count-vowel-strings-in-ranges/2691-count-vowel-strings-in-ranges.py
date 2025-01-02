class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowel = {'a', 'e', 'i', 'o', 'u'}

        def valid(s):
            return s[0] in vowel and s[-1] in vowel

        prefix[0] = 1 if valid(words[0]) else 0

        for i in range(1, len(words)):
            prefix.append(prefix[-1] + (1 if valid(words[i]) else 0))

        # print(prefix)
        res = []
        
        for x, y in queries:
            addOn = 1 if valid(words[x]) else 0
            ans = prefix[y] - prefix[x] + addOn
            res.append(ans)

        return res                    

        


        