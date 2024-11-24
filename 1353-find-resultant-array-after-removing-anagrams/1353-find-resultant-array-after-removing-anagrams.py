class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        for i in range(1, len(words)):
            if sorted(words[i]) == sorted(words[i-1]):
                words[i], words[i-1] = words[i-1], words[i]
                words[i-1] = "#"

        return [x for x in words if x != "#"]        

        