class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        resMap = {}

        for i,w in enumerate(arr):
            if w not in resMap:
                resMap[w] = [i,1]
            else:
                resMap[w][1] += 1

        heap = []

        for n,v in resMap.items():
            if v[1] == 1:
                heapq.heappush(heap, [v[0],n])  
        
        while heap and k > 1:
            heapq.heappop(heap)
            k -= 1

        if heap:
            return heapq.heappop(heap)[1]   

        return ""   
