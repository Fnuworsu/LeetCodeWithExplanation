class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, components):
            if node not in visited:
                components.append(node)

            visited.add(node)

            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb, components)

        def complete(components):
            nCount, eCount = len(components), 0

            if not components: return False

            for node in components:
                eCount += len(graph[node])
            eCount //=2
            
            return eCount == (nCount * (nCount - 1)) // 2
        res = 0

        for node in range(n):
            components = []
            dfs(node, components)
            print(node, "=>",components)

            if complete(components):
                res += 1

        return res                         
                                    
        