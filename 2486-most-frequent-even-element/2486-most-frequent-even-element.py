class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        resMap = defaultdict(int)

        for n in nums:
            if not n % 2:
                resMap[n] += 1

        pq = []

        for k,v in resMap.items():
            pq.append((k,-v))

        pq.sort(key=lambda x:(x[1], x[0]))

        return pq[0][0] if pq else -1   
        