class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        b a c a b c b b

        c a
        """
        if not s:
            return 0

        q = deque([s[0]])
        cache = set(s[0])
        maxLen = 1

        for i in range(1, len(s)):
            if s[i] in cache:
                maxLen = max(len(q), maxLen)
                while q and q[0] != s[i]:
                    cache.remove(q.popleft())
                
                cache.remove(q.popleft())
            
            q.append(s[i])
            cache.add(s[i])
        
        return max(maxLen, len(q))
                
