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
    
    def search(self, prefix):
        def dfs(node, path, res):
            if len(res) == 3:
                return
            if node.end:
                res.append("".join(path[:]))
            
            for k,v in node.children.items():
                path.append(k)
                dfs(v, path, res)
                path.pop()
        
        node = self.root

        for c in prefix:
            node = node.children[c]

        res = []
        dfs(node, list(prefix), res)

        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()

        for p in products:
            trie.add(p)
        
        prefix = ""
        res = []

        for c in searchWord:
            prefix += c
            res.append(trie.search(prefix))
        
        return res