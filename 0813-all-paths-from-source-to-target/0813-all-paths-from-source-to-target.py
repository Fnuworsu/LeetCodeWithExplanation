class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def backtrack(node, stack):
            nonlocal res
            # print(res,' => ',stack)
            if node == len(graph)-1:
                res.append(stack[:])
                return

            for nb in graph[node]:
                stack.append(nb)
                backtrack(nb,stack)
                stack.pop()

        backtrack(0,[0])

        return res        


              
        