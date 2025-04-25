class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        displaces = 0
        c1, c2 = Counter(s1), Counter(s2)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                displaces += 1
                if c1[s1[i]] != c2[s1[i]] or c1[s2[i]] != c2[s2[i]]:
                    return False

        return displaces <= 2 
        