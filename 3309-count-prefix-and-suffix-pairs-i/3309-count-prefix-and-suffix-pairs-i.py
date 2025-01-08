class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        #Rolling hash
        toInt = lambda x : ord(x) - ord('a') + 1
        base = 31
        mod = 10**9 + 7
        ps = defaultdict(int)
        res = 0

        for w in words:
            prefix = 0
            suffix = 0

            for i in range(len(w)):
                prefix = (prefix * base + toInt(w[i])) % mod
                suffix = (suffix * base + toInt(w[~i])) % mod
                # print(w, '=>', (prefix,suffix))
                res += ps[(prefix, suffix)]
            ps[(prefix, suffix)] += 1

        return res        


        