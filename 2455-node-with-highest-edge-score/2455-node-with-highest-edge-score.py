class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        """
        [1,0,0,0,0,7,7,5]
         0,1,2,3,4,5,6,7
         {
            1:0
            0:1,2,3,4
            7:5,6
            5:7
         }
        """
        graph = defaultdict(int)

        for node, out in enumerate(edges):
            graph[out] += node

        res = []

        for k,v in graph.items():
            res.append((k,v))

        res.sort(key=lambda x:(-x[1], x[0]))
        return res[0][0]