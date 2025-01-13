class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""

        for w in words:
            prefix += w
            if prefix == s:
                return True
        
        return False