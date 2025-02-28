class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = ''
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root

        for c in word:
            curr = curr.children[c]
        
        curr.end = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for w in words:
            trie.add(w)
        
        rows, cols = len(board), len(board[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def outBounds(r,c):
            return r < 0 or r > rows-1 or c < 0 or c > cols-1
        
        def dfs(r,c,node,cache):
            nonlocal res

            char = board[r][c]
            if char not in node.children:
                return 

            node = node.children[char]
            cache.add((r,c))

            if node.end:
                res.add(node.word)
                node.end = False
            
            for dr,dc in dirs:
                nr, nc = r + dr, c + dc

                if outBounds(nr,nc) or (nr,nc) in cache:
                    continue
                
                dfs(nr,nc,node,cache)

            cache.remove((r,c))
        
        res = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(r,c,trie.root,set())
        
        return list(res)