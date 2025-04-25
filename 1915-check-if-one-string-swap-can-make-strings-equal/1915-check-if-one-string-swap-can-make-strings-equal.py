class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(set(s1)) != len(set(s2)):
            return False
        shift = 0

        for c1,c2 in zip(s1, s2):
            if c1 != c2:
                shift += 1
        
        return shift <= 2