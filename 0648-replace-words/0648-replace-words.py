class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            curr = curr.children[c]
        
        curr.end = True
    
    def find(self, word):
        curr = self.root
        prefix = ""

        for c in word:
            if c not in curr.children:
                break
            curr = curr.children[c]
            prefix += c
            if curr.end:
                return prefix
        
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        res = []

        for root in dictionary:
            trie.insert(root)
        
        for word in sentence.split():
            res.append(trie.find(word))
        
        return " ".join(res)
        