class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            curr = curr.children[c]

        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(w,root):
            for i,c in enumerate(w):  
                if c == '.':
                    for child in root.children.values():
                        if dfs(w[i+1:], child):
                            return True
                    return False
                if c not in root.children:
                    return False    
                root = root.children[c]
            return root.end

        return dfs(word, curr)         
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)