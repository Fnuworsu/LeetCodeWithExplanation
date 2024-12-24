class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            curr = curr.children[c]

        curr.isEnd = True   

    def search(self, word: str) -> bool:
        def dfs(root, j, w):
            curr = root

            for i in range(j, len(w)):
                if w[i] == ".":
                    for child in curr.children.values():
                        if dfs(child, i+1, w):
                            return True
                    return False

                else:
                    if w[i] not in curr.children:
                        return False

                    curr = curr.children[w[i]]

            return curr.isEnd                    

        return dfs(self.root, 0, word)                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)