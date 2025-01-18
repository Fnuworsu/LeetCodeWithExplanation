class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.end = True
    
    def isPrefix(self, prefix):
        def dfs(node, path, res):
            if node.end:
                res.append("".join(path[:]))
            
            for k,v in node.children.items():
                path.append(k)
                dfs(v, path, res)
                path.pop()
        
        curr = self.root

        for c in prefix:
            curr = curr.children[c]

        res = []
        dfs(curr, list(prefix), res)

        return res

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        trie = Trie()
        words = sentence.split()
        hMap = {}

        for i,w in enumerate(words):
            if w in hMap:
                continue
            hMap[w] = i+1

        for w in words:
            if w[0] == searchWord[0]:
                trie.add(w)
        
        acc = trie.isPrefix(searchWord)
        # print(acc)
        res = float('inf')

        for p in acc:
            res = min(res, hMap[p])
        
        return res if res != float('inf') else -1
        