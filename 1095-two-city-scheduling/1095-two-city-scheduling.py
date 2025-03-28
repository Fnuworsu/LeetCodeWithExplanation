class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """

        """
        arr = []
        idx = len(costs) // 2
        res = 0

        for i in range(2 * idx):
            a,b = costs[i]
            arr.append(((a-b), i))
        
        arr.sort()

        for x in arr[:idx]:
            res += costs[x[1]][0]
        
        for x in arr[idx:]:
            res += costs[x[1]][1]
        
        return res
            
        