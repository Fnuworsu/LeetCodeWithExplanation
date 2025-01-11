class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        resMap = defaultdict(int)

        for n in nums:
            resMap[n] += 1

        pq = []

        for k,v in resMap.items():
            pq.append((v,k))

        pq.sort(key=lambda x:(x[0], -x[1]))
        res = []

        for v,k in pq:
            for _ in range(v):
                res.append(k)

        return res           
        