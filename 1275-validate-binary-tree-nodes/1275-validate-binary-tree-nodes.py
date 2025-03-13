class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        degree = [0 for _ in range(n)]

        i = 0
        for l,r in zip(leftChild, rightChild):
            if l >= 0:
                degree[l] += 1
                graph[i].append(l)
            if r >= 0:
                degree[r] += 1
                graph[i].append(r)
            i += 1

        pq = deque([])

        for node in range(len(degree)):
            if degree[node] == 0:
                pq.append(node)
        # print(graph)
        # print(degree)
        # print(pq)
        if len(pq) > 1 or not pq:
            return False
        
        while pq:
            for _ in range(len(pq)):
                node = pq.popleft()
                for nb in graph[node]:
                    degree[nb] -= 1
                    if degree[nb] != 0:
                        return False
                    pq.append(nb)
        # print(degree)
        for d in degree:
            if d != 0:
                return False
        
        return True