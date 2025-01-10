class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = defaultdict(int)
        
        for c in s:
            hmap[c] += 1

        pq = []   

        for k,v in hmap.items():
            heapq.heappush(pq, (-v,k))

        res = ""

        while pq:
            freq, c = heapq.heappop(pq)
            newChar = (-1 * freq) * c

            res += newChar

        return res    



