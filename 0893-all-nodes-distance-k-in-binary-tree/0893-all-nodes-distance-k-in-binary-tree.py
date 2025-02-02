# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        q = deque([root])

        while q:
            currLevel = len(q)

            for _ in range(currLevel):
                node = q.popleft()
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    q.append(node.right)
        # print(graph)

        pq = deque([target.val])
        steps = 0
        visited = set()
        res = []

        while pq:
            for _ in range(len(pq)):
                # print(pq)
                node = pq.popleft()
                visited.add(node)
                if steps == k:
                    res.append(node)
                    continue
                
                for nb in graph[node]:
                    if nb not in visited:
                        pq.append(nb)
            steps += 1       
        return res
        