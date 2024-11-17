class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        point = [x,y]
        """
        minHeap = [] #[d, (x,y)]

        for x, y in points:
            d = x**2 + y**2
            minHeap.append([d, [x, y]])

        heapify(minHeap)
        res = []

        while k > 0:
            val = heappop(minHeap) #[d, (x,y)]
            res.append(val[1])

            k -= 1
        # print(res)
        return res    


        