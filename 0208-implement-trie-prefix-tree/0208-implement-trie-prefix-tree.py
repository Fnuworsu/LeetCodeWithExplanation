class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()             

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            curr = curr.children[c]
        
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]  
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            curr = curr.children[c]

        res = []

        self.dfs(curr, list(prefix), res)
        # print(res)
        return True if res else False
        
    def dfs(self, node, path, res):
        if node.end:
            res.append(path[:])
        
        for k,v in node.children.items():
            path.append(k)
            # print(path)
            self.dfs(v, path, res)
            path.pop()



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)