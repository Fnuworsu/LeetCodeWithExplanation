class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        curr = self.root 
        for c in w:
            curr = curr.children[c]
        curr.end = True

    def isPrefix(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True                  

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #Using trie
        res = 0

        for w in words:
            if w[0] != pref[0]:
                continue
            if len(pref) > len(w):
                continue    
            
            trie = Trie()
            trie.add(w)

            if trie.isPrefix(pref):
                res += 1

        return res        