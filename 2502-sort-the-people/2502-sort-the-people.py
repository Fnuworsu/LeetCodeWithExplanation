class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pq = []

        for n,h in zip(names, heights):
            pq.append((-h,n))
        
        pq.sort()

        return [x[1] for x in pq]