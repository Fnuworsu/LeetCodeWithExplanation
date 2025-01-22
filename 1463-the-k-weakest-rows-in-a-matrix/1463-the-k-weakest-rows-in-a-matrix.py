class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        pq = []

        for r in range(rows):
            freq = Counter(mat[r])
            acc = (freq[1], r)

            pq.append(acc)
        
        pq.sort(key=lambda x:(x[0], x[1]))
        pq = deque(pq)
        res = []

        while k:
            freq, r = pq.popleft()
            res.append(r)

            k -= 1
        
        return res

        