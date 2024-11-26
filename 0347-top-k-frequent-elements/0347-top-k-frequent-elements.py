class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = defaultdict(int)
        freq = [[] for x in range(len(nums)+1)]

        for n in nums:
            freqCount[n] += 1

        for n, v in freqCount.items():
            freq[v].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        