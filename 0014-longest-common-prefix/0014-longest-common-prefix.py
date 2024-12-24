class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]

        curr.isEnd = True

    def prefix(self,word):
        curr = self.root
        res = ""

        for c in word:
            if len(curr.children.values()) > 1 or curr.isEnd:
                break
            if c in curr.children:
                res += c
                curr = curr.children[c]

        return res        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for word in strs:
            trie.insert(word)

        res = trie.prefix(strs[0])

        return res    

        