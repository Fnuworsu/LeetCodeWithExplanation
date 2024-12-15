class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        pq = [(-k,v) for k,v in count.items()]
        heapq.heapify(pq)
        # print(pq)

        while k > 1:
            curr = heapq.heappop(pq)
            if curr[1] - 1 > 0:
                heapq.heappush(pq, (curr[0], curr[1]-1))

            k -= 1    

        return -heapq.heappop(pq)[0]    
        