class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        n = len(beginWord)

        for w in wordList:
            for i in range(n):
                node = w[:i] + "#" + w[i+1:]
                graph[node].append(w)
        
        q = deque([beginWord])
        seen = set()
        level = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node in seen:
                    continue
                seen.add(node)

                for i in range(n):
                    new_node = node[:i] + "#" + node[i+1:]
                    for nb in graph[new_node]:
                        if nb == endWord:
                            level += 1
                            return level
                        if nb in seen:
                            continue
                        q.append(nb)
            
            level += 1
        
        return 0

