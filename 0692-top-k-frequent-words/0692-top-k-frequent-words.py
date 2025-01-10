class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        resMap = defaultdict(int)
        
        for w in words:
            resMap[w] += 1

        pq = []    

        for w,v in resMap.items():
            pq.append((-v,w))

        pq.sort(key=lambda x:(x[0], x[1]))   
        res = []

        while k > 0:
            addOn = heapq.heappop(pq)
            res.append(addOn[1])
            k -= 1

        return res     
        