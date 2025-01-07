class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, w):
        curr = self.root
        for c in w:
            curr = curr.children[c]
            curr.freq += 1
        curr.end = True

    def isSubtr(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.freq > 1        


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        trie = Trie()
        words.sort(key=lambda x:len(x))
        res = []


        for w in words:
            for i in range(len(w)):
                trie.add(w[i:])

        for w in words:
            if trie.isSubtr(w):
                res.append(w)  

        return res              

               
        