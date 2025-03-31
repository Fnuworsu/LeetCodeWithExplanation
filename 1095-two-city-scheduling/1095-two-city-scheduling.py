class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        i = len(costs) //2
        costs.sort(key=lambda x: x[0] - x[1])
        res = 0
        
        for n in costs[:i]:
            res += n[0]
        
        for n in costs[i:]:
            res += n[1]

        return res
        