class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        Set = set()

        for r in range(len(s)):
            if s[r] not in Set:
                Set.add(s[r])
                maxLen = max(maxLen, len(Set))
            else:
                while s[r] in Set:
                    Set.remove(s[l])
                    l += 1
                Set.add(s[r])  

        return maxLen              